import re
def get_input(file):
    input = []
    with open(file) as f:
        for line in f:
            input.append(line.strip())
    return input

def solution_part1(input):
    sum = 0
    for row in input:
        clean_input = re.findall('\d', row)
        if (len(clean_input) == 0):
            continue
        sum += int(clean_input[0]+clean_input[-1])
    return sum

def solution_part2(input):
    sum = 0
    dic_numbers = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    for row in input:
        row_dic = {}
        for key in dic_numbers:
            if (key in row):
                row_dic[row.find(key)] = dic_numbers[key]
        for char in row:
            if (char.isdigit()):
                row_dic[row.find(char)] = char
        dic_sorted = dict(sorted(row_dic.items()))
        min_value_key = list(dic_sorted)[0]
        max_value_key = list(dic_sorted)[-1]
        sum += int((row_dic.get(min_value_key) + row_dic.get(max_value_key)))
    return sum
        
    
            
        

input = get_input('./input')
print(f'The Solution of part 1 is: {solution_part1(input)}')
print(f'The Solution of part 2 is: {solution_part2(input)}')