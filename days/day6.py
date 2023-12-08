import time, numpy
def get_input(file):
    input = []
    with open(file) as f:
        for line in f:
            input.append(line.strip())
    return input

def solution_part1(input):
    sums = []
    times = input[0].split()[1:]
    distances = input[1].split()[1:]
    
    for index, time in enumerate(times):
        beated_record = 0
        distance = distances[index]
        for i in range(0, int(time)):
            mms = i
            ttr = int(time) - i
            if mms * ttr > int(distance):
                beated_record += 1
        sums.append(beated_record)
    return numpy.prod(sums)

def solution_part2(input):
    beated_record = 0
    time = "".join(input[0].split()[1:])
    distance = "".join(input[1].split()[1:])
    for i in range(0, int(time)):
        mms = i
        ttr = int(time) - i
        if mms * ttr > int(distance):
            beated_record += 1
    return beated_record

input = get_input('./input')
timer = time.perf_counter()
print(f'The Solution of part 1 is: {solution_part1(input)} | solved in {time.perf_counter()-timer:.5f}s')
timer = time.perf_counter()
print(f'The Solution of part 2 is: {solution_part2(input)} | solved in {time.perf_counter()-timer:.5f}s')