import re

def get_input(file):
    input = []
    with open(file) as f:
        for line in f:
            input.append(line.strip())
    return input

def solution_part1(input):
    sum = 0
    
    dic_colors_limits = {
            "red": 12,
            "green": 13,
            "blue": 14
        }
    for row in input:
        
        dic_colors = {
            "red": 0,
            "blue": 0,
            "green": 0,
        }
        
        game_id = row.split(": ")[0].split(" ")[1]
        rounds = row.split(": ")[1].split("; ")
        
        for round in rounds:
            color_combinations = round.split(", ")
            for color_combination in color_combinations:
                number, color = color_combination.split(" ")
                if (int(dic_colors[color]) < int(number)):
                    dic_colors[color] = int(number)
        is_valid = True
        for color in dic_colors:
            if (dic_colors[color] > dic_colors_limits[color]):
                is_valid = False
        if (is_valid):
            sum += int(game_id)
    return sum

def solution_part2(input):
    sum = 0
    
    for row in input:
        
        dic_colors = {
            "red": 0,
            "blue": 0,
            "green": 0,
        }
        
        rounds = row.split(": ")[1].split("; ")
        
        for round in rounds:
            color_combinations = round.split(", ")
            for color_combination in color_combinations:
                number, color = color_combination.split(" ")
                if (int(dic_colors[color]) < int(number)):
                    dic_colors[color] = int(number)
        
        power = 1
        for color in dic_colors:
            power *= dic_colors[color]
        sum += power
    return sum

input = get_input('./input')
print(f'The Solution of part 1 is: {solution_part1(input)}')
print(f'The Solution of part 2 is: {solution_part2(input)}')