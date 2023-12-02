def get_input(file):
    input = []
    with open(file) as f:
        for line in f:
            input.append(line.strip())
    return input

def solution_part1(input):
    return input

def solution_part2(input):
    return input

input = get_input('input')
print(f'The Solution of part 1 is: {solution_part1(input)}')
print(f'The Solution of part 2 is: {solution_part2(input)}')