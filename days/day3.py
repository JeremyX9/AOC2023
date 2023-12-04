import random
import re
import string
def get_input(file):
    input = []
    with open(file) as f:
        for line in f:
            input.append(line.strip())
    return input

def solution_part1(raw_input):
    input = raw_input.copy()
    sum = 0
    
    dot_array = [['.' for _ in range(len(input[0]))] for _ in range(len(input))]
    for row, line in enumerate(input):
        input[row] = re.sub('[^A-Za-z0-9]', '.', line)
        for position in re.finditer('[^A-Za-z0-9.]', line):
            for i in range(-1, 2):
                for j in range(-1, 2):
                    dot_array[row+i][position.start()+j] = '#'
    for row, line in enumerate(dot_array):
        for column, char in enumerate(line):
            column_copy = column
            if char == '#':
                current_char = input[row][column]
                if (input[row][column].isdigit()):
                    while current_char.isdigit():
                        column_copy -= 1
                        current_char = input[row][column_copy]
                    column_copy += 1
                    current_char = input[row][column_copy]
                    
                    number_to_add = ''
                    while current_char.isdigit():
                        number_to_add += current_char
                        input_list = list(input[row])
                        input_list[column_copy] = '.'
                        input[row] = ''.join(input_list)
                        column_copy += 1
                        if (column_copy == len(input[row])):
                            break
                        current_char = input[row][column_copy]
                    sum += int(number_to_add)
    return sum

def solution_part2(raw_input):
    input = raw_input.copy()
    sum = 0
    
    dot_array = [['.' for _ in range(len(input[0]))] for _ in range(len(input))]
    dot_uid_dic = {}
    for row, line in enumerate(input):
        input[row] = re.sub('[^A-Za-z0-9]', '.', line)
        for position in re.finditer('\*', line):
            uid = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
            dot_uid_dic[uid] = {}
            dot_uid_dic[uid]["count"] = 0
            dot_uid_dic[uid]["sum"] = 1
            for i in range(-1, 2):
                for j in range(-1, 2):
                    dot_array[row+i][position.start()+j] = uid
    
    print(dot_uid_dic)
    for row, line in enumerate(dot_array):
        for column, char in enumerate(line):
            column_copy = column
            if char != '.':
                current_char = input[row][column]
                if (input[row][column].isdigit()):
                    while current_char.isdigit():
                        column_copy -= 1
                        current_char = input[row][column_copy]
                    column_copy += 1
                    current_char = input[row][column_copy]
                    
                    number_to_add = ''
                    while current_char.isdigit():
                        number_to_add += current_char
                        input_list = list(input[row])
                        
                        input_list[column_copy] = '.'
                        input[row] = ''.join(input_list)
                        column_copy += 1
                        if (column_copy == len(input[row])):
                            break
                        current_char = input[row][column_copy]
                    dot_uid_dic[char]["count"] += 1
                    dot_uid_dic[char]["sum"] *= int(number_to_add)
    for dic_entry in {k:v for (k,v) in dot_uid_dic.items() if v["count"] == 2}:
        sum += dot_uid_dic[dic_entry]["sum"]
    return sum

input = get_input('./input')
print(f'The Solution of part 1 is: {solution_part1(input)}')
print(f'The Solution of part 2 is: {solution_part2(input)}')