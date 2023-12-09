import time
def get_input(file):
    input = []
    with open(file) as f:
        for line in f:
            input.append(line.strip())
    return input

def solution_part1(input):
    sum = 0
    card_list = []
    strength = "23456789TJQKA"
    for line in input:
        card, bid = line.split(" ")
        cards = list(card)
        cards = [strength.index(c) for c in cards]
        
        type = 0 
        
        amounts = [cards.count(i) for i in range(13)]
        if 5 in amounts: type =  6
        elif 4 in amounts: type = 5
        elif 3 in amounts and 2 in amounts: type = 4
        elif 3 in amounts: type = 3
        elif amounts.count(2) == 2: type = 2
        elif 2 in amounts: type = 1
        elif 1 in amounts: type = 0
        
        card_list.append((type, cards, bid))
    card_list = sorted(card_list)
    for rank, card_list_entry in enumerate(card_list, start=1):
        sum += int(card_list_entry[2]) * rank
    return sum

def solution_part2(input):
    sum = 0
    card_list = []
    strength = "J23456789TQKA"
    for line in input:
        card, bid = line.split(" ")
        cards = list(card)
        cards = [strength.index(c) for c in cards]
        
        type = 0 
        
        amounts = [cards.count(i) for i in range(13)]
        j = amounts.pop(0)
        amounts[amounts.index(max(amounts))] += j
        if 5 in amounts: type =  6
        elif 4 in amounts: type = 5
        elif 3 in amounts and 2 in amounts: type = 4
        elif 3 in amounts: type = 3
        elif amounts.count(2) == 2: type = 2
        elif 2 in amounts: type = 1
        elif 1 in amounts: type = 0
        
        card_list.append((type, cards, bid))
    card_list = sorted(card_list)
    for rank, card_list_entry in enumerate(card_list, start=1):
        sum += int(card_list_entry[2]) * rank
    return sum

input = get_input('./input')
timer = time.perf_counter()
print(f'The Solution of part 1 is: {solution_part1(input)} | solved in {time.perf_counter()-timer:.5f}s')
timer = time.perf_counter()
print(f'The Solution of part 2 is: {solution_part2(input)} | solved in {time.perf_counter()-timer:.5f}s')