import time
def get_input(file):
    input = []
    with open(file) as f:
        return [list(map(int, line.strip().split())) for line in f]

def rec(s):
    if len(set(s)) == 1: return s[0]
    next = rec([b - a for a, b in zip(s, s[1:])])
    return next + s[-1]

def rec2(s):
    if len(set(s)) == 1: return s[0]
    next = rec2([b - a for a, b in zip(s, s[1:])])
    return s[0] - next

def solution_part1(input):
    return sum(rec(s) for s in input)

def solution_part2(input):
    return sum(rec2(s) for s in input)

input = get_input('./input')
timer = time.perf_counter()
print(f'The Solution of part 1 is: {solution_part1(input)} | solved in {time.perf_counter()-timer:.5f}s')
timer = time.perf_counter()
print(f'The Solution of part 2 is: {solution_part2(input)} | solved in {time.perf_counter()-timer:.5f}s')