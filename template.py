import time
def get_input(file):
    input = []
    with open(file) as f:
        for line in f:
            input.append(line.strip())
    return input

def solution_part1(input):
    sum = 0
    return sum

def solution_part2(input):
    sum = 0
    return sum

input = get_input('./input')
timer = time.perf_counter()
print(f'The Solution of part 1 is: {solution_part1(input)} | solved in {time.perf_counter()-timer:.5f}s')
timer = time.perf_counter()
print(f'The Solution of part 2 is: {solution_part2(input)} | solved in {time.perf_counter()-timer:.5f}s')