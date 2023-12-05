def get_input(file):
    input = []
    with open(file) as f:
        for line in f:
            input.append(line.strip())
    return input

def solution_part1(input):
    sum = 0
    for line in input:
        winning_numbers, your_numbers = [_.split(" ") for _ in line.replace("  ", " ").split(": ")[1].split(" | ")]
        len_of_set = len(set(winning_numbers) & set(your_numbers))
        if (len_of_set != 0):
            sum += (2**(len(set(winning_numbers) & set(your_numbers))-1))
    return sum

def solution_part2(input):
    sum = 0
    game_dic = {}
    instance_dic = {}
    for line in input:
        game_id, board = line.replace("   ", " ").replace("  ", " ").split(": ")
        game_id = game_id.split(" ")[1]
        winning_numbers, your_numbers = [_.split(" ") for _ in board.split(" | ")]
        len_of_set = len(set(winning_numbers) & set(your_numbers))
        game_dic[game_id] = len_of_set
        instance_dic[game_id] = 1
    print(game_dic)
    while instance_dic != {}:
        instance_dic_element_index = next(iter(instance_dic))
        sum += instance_dic[instance_dic_element_index]
        for i in range(0, game_dic[instance_dic_element_index]):
            if (str(int(instance_dic_element_index)+1+i) in instance_dic):
                instance_dic[str(int(instance_dic_element_index)+1+i)] += instance_dic[instance_dic_element_index]
        del instance_dic[instance_dic_element_index]
    return sum
 
input = get_input('./input')
print(f'The Solution of part 1 is: {solution_part1(input)}')
print(f'The Solution of part 2 is: {solution_part2(input)}')