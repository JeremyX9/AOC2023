import time

def get_input(file):
    with open(file) as f:
        file = f.read().split("\n\n")
    return file

def solution_part1(input):
    seeds_to_plant = input[0].replace("seeds: ", "").split(" ")
    blocks = [{"seeds": [[y for y in x.split()] for x in block.split('\n')[1:] if x]} for block in [n for i, n in enumerate(input) if i > 0]]
     
    locations = []
    for seed in seeds_to_plant:
        correspsonding_value = int(seed)
        for block in blocks:
            for action in block["seeds"]:
                dest, source, range = int(action[0]), int(action[1]), int(action[2])
                if (not source > correspsonding_value and not source+range-1 < correspsonding_value):
                    correspsonding_value = dest + (correspsonding_value - source)
                    break
        locations.append(correspsonding_value)
    return min(locations)

# not valid with all inputs
def solution_part2(input):
    seeds_to_plant_raw = input[0].replace("seeds: ", "").split(" ")
    seed_pairs = [[int(seeds_to_plant_raw[i]), int(seeds_to_plant_raw[i]) + int(seeds_to_plant_raw[i+1])-1] for i in range(0, len(seeds_to_plant_raw), 2)]
    blocks = [{"seeds": [[y for y in x.split()] for x in block.split('\n')[1:] if x]} for block in [n for i, n in enumerate(input) if i > 0]]
    
    locations = []
    for lowest, highest in seed_pairs:
        while lowest-1 < highest:
            seed = lowest
            lowest = -1
            for block in blocks:
                for action in block["seeds"]:
                    dest, source, rng = int(action[0]), int(action[1]), int(action[2])
                    if (not source > seed and not source+rng-1 < seed):
                        if lowest == -1: lowest = source + rng 
                        seed = dest + (seed - source)
                        break
            locations.append(seed)
    return min(locations)
input = get_input('./input')
timer = time.perf_counter()
print(f'The Solution of part 1 is: {solution_part1(input)} | solved in {time.perf_counter()-timer:.5f}s')
timer = time.perf_counter()
print(f'The Solution of part 2 is: {solution_part2(input)} | solved in {time.perf_counter()-timer:.5f}s')