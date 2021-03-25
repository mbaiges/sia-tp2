import random
from constants import min_height, max_height

def get_rand_item(items):
    idx = random.randint(0, len(items))
    return items[idx]

def get_random_character(all_items, char_gen):
    weapon = get_rand_item(all_items.weapons)
    boots = get_rand_item(all_items.boots)
    helmet = get_rand_item(all_items.helmets)
    gloves = get_rand_item(all_items.gloves)
    breastplate = get_rand_item(all_items.breastplates)

    height = random.uniform(min_height, max_height)

    gens = [height, weapon, boots, helmet, gloves, breastplate]

    return char_gen(gens)

def get_initial_population(all_items, char_gen, n):
    characters = []
    count = 0

    while count < n:
        char = get_random_character(all_items, char_gen)
        characters.append(char)
        count += 1

    return characters