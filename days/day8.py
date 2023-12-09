import math
import time
import re 
def get_input(file):
    input = []
    with open(file) as f:
        return f.read()
def solution_part1(input):
    steps = list(input.split("\n\n")[0])
    way = {}
    for line in input.split("\n\n")[1].split("\n"):
        match = re.findall(r"[A-Z]{3}", line)
        way[match[0]] = {"L": match[1], "R": match[2]}
    count = 0
    current_step_symbol = "AAA"
    while current_step_symbol != "ZZZ":
        count += 1
        step = steps[count % len(steps)-1]
        if (step == "L"):
            current_step_symbol = way[current_step_symbol]["L"]
        elif (step == "R"):
            current_step_symbol = way[current_step_symbol]["R"]
    return count

def solution_part2(input):
    steps = list(input.split("\n\n")[0])
    way = {}
    for line in input.split("\n\n")[1].split("\n"):
        match = re.findall(r"[A-Z]{3}", line)
        way[match[0]] = {"L": match[1], "R": match[2]}
    counts = []
    start_step_symbols = [e for e in way.keys() if e.endswith("A")]
    
    for step in start_step_symbols:
        current_symbol = step
        count = 0
        while current_symbol.endswith("Z") == False:
            count += 1
            direction = steps[count % len(steps)-1]
            if (direction == "L"):
                current_symbol = way[current_symbol]["L"]
            elif (direction == "R"):
                current_symbol = way[current_symbol]["R"]
        counts.append(count)
        
        
    return math.lcm(*counts)

input = get_input('./input')
timer = time.perf_counter()
print(f'The Solution of part 1 is: {solution_part1(input)} | solved in {time.perf_counter()-timer:.5f}s')
timer = time.perf_counter()
print(f'The Solution of part 2 is: {solution_part2(input)} | solved in {time.perf_counter()-timer:.5f}s') 