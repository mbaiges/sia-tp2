from models import Warrior, Archer, Defender, Infiltrate, Setup
from stops import Time

from utils import read_all_items

characters_classes = {
    'warrior': Warrior,
    'archer': Archer,
    'defender': Defender,
    'infiltrate': Infiltrate
}

crossovers = {
    'one_point': 'algo',
    'two_point': 'algo',
    'anular': 'algo',
    'uniform': 'algo'
}

mutations = {
    'gen': 'algo',
    'multi_limited': 'algo',
    'multi_uniform': 'algo',
    'full': 'algo'
}

selections = {
    'elite': 'algo',
    'roulette': 'algo',
    'universal': 'algo',
    'boltzmann': 'algo',
    'det_tournaments': 'algo',
    'prob_tournaments': 'algo',
    'ranking': 'algo'
}

implementations = {
    'fill_all': 'algo',
    'fill_parent': 'algo'
}

stops = {
    'time': Time,
    'gens': Time,
    'acceptable': Time,
    'struct': Time,
    'content': Time
}

def get_setup(config):

    # Character class

    print(f'Character class: {config.character_class}')
    character_class_constructor = characters_classes.get(config.character_class, None)

    if character_class_constructor is None:
        print(f'Error: Character class "{config.character_class}" does not exist')
        exit(1)

    # Genetic operators

    ## Crossover

    crossover = crossovers.get(config.crossover, None)
    if crossover is None:
        print(f'Error: Crossover method "{config.crossover}" does not exist')
        exit(1)

    ## Mutation

    mutation = mutations.get(config.mutation, None)
    if mutation is None:
        print(f'Error: Crossover method "{config.mutation}" does not exist')
        exit(1)
    
    # Parents selection and children replacement

    ## A

    A = config.A
    if not (type(A) == int or type(A) == float):
        print('Error: A must be a number')
        exit(1)
    A = float(A)
    if A < 0 or A > 1:
        print('Error: A must be in range [0.0-1.1]')
        exit(1)

    ## B

    B = config.B
    if not (type(B) == int or type(B) == float):
        print('Error: B must be a number')
        exit(1)
    B = float(B)
    if B < 0 or B > 1:
        print('Error: B must be in range [0.0-1.1]')
        exit(1)

    ## Method 1

    method1 = selections.get(config.method1, None)
    if method1 is None:
        print(f'Error: Selection method 1 "{config.method1}" does not exist')
        exit(1)

    ## Method 2

    method2 = selections.get(config.method2, None)
    if method2 is None:
        print(f'Error: Selection method 2 "{config.method2}" does not exist')
        exit(1)

    ## Method 3

    method3 = selections.get(config.method3, None)
    if method3 is None:
        print(f'Error: Selection method 3 "{config.method3}" does not exist')
        exit(1)

    ## Method 4

    method4 = selections.get(config.method4, None)
    if method4 is None:
        print(f'Error: Selection method 4 "{config.method4}" does not exist')
        exit(1)

    # Implementation

    implementation = implementations.get(config.implementation, None)
    if implementation is None:
        print(f'Error: Implementation method "{config.implementation}" does not exist')
        exit(1)

    # Stop

    stop = stops.get(config.stop, None)
    if stop is None:
        print(f'Error: Stop method "{config.stop}" does not exist')
        exit(1)

    if config.stop == 'time':
        max_time = config.max_time
        if not (type(max_time) == int or type(max_time) == float):
            print('Error: max_time must be a number')
            exit(1)
        max_time = float(max_time)
        if max_time <= 0:
            print('Error: max_time must be greater than 0')
            exit(1)

        stop = stop(config.max_time)
    else:
        stop = stop()

    # Items loading

    all_items = read_all_items(config.items_dataset_path, config.items_dataset_filenames)
    print("Items loaded")

    return Setup(all_items, crossover, mutation, A, B, method1, method2, method3, method4, implementation, stop, character_class_constructor, config.initial_population)