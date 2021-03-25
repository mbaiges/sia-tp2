from models import Warrior, Archer, Defender, Infiltrate, Setup
from selections import Elite, Roulette, Universal, Boltzmann
from crossovers import OnePoint, TwoPoints, Anular, Uniform
from stops import Time, Generations, Acceptable

from utils import read_all_items

characters_classes = {
    'warrior': Warrior,
    'archer': Archer,
    'defender': Defender,
    'infiltrate': Infiltrate
}

crossovers = {
    'one_point': OnePoint,
    'two_points': TwoPoints,
    'anular': Anular,
    'uniform': Uniform
}

mutations = {
    'gen': 'algo',
    'multi_limited': 'algo',
    'multi_uniform': 'algo',
    'full': 'algo'
}

selections = {
    'elite': Elite,
    'roulette': Roulette,
    'universal': Roulette,
    'boltzmann': Roulette,
    'det_tournaments': Roulette,
    'prob_tournaments': Roulette,
    'ranking': Roulette
}

implementations = {
    'fill_all': 'algo',
    'fill_parent': 'algo'
}

stops = {
    'time': Time,
    'gens': Generations,
    'acceptable': Acceptable,
    'struct': Time,
    'content': Time
}

def get_setup(config):

    # Character class

    character_class_constructor = characters_classes.get(config.character_class, None)

    if character_class_constructor is None:
        print(f'Error: Character class "{config.character_class}" does not exist')
        exit(1)

    # Parents selection and children replacement

    ## K

    K = config.K
    if not type(K) == int:
        print('Error: K must be a number')
        exit(1)
    K = float(K)
    if K <= 0:
        print('Error: A must be greater than 0')
        exit(1)    

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

    method1 = method1()

    ## Method 2

    method2 = selections.get(config.method2, None)
    if method2 is None:
        print(f'Error: Selection method 2 "{config.method2}" does not exist')
        exit(1)

    method2 = method2()

    ## Method 3

    method3 = selections.get(config.method3, None)
    if method3 is None:
        print(f'Error: Selection method 3 "{config.method3}" does not exist')
        exit(1)

    method3 = method3()

    ## Method 4

    method4 = selections.get(config.method4, None)
    if method4 is None:
        print(f'Error: Selection method 4 "{config.method4}" does not exist')
        exit(1)

    method4 = method4()

    # Genetic operators

    ## Crossover

    crossover = crossovers.get(config.crossover, None)
    if crossover is None:
        print(f'Error: Crossover method "{config.crossover}" does not exist')
        exit(1)

    ## they all need params
    crossover_params = config.crossover_params

    if crossover_params is None:
        print("Error: Crossover params missing")
        exit(1)

    if config.crossover == 'one_point':
        p = crossover_params['p']
        if p is None:
            print("Error: Missing p param at crossover")
            exit(1)
        elif not type(p) == int:
            print('Error: p must be an integer')
            exit(1)
        p = int(p)
        if p < 0 or p > 5:
            print('Error: p must be in range [0 - 5]')
            exit(1)
        crossover = crossover(p)
    elif config.crossover == 'two_points':
        p1 = crossover_params['p1']
        p2 = crossover_params['p2']
        
        if p1 is None:
            print("Error: Missing p1 param at crossover")
            exit(1)
        elif p2 is None:
            print("Error: Missing p2 param at crossover")
            exit(1)
        elif not type(p1) == int or not type(p2) == int:
            print('Error: p1 and p2 must be integers')
            exit(1)
        p1 = int(p1)
        p2 = int(p2)
        if p1 < 0 or p1 > 5 or p2 < 0 or p2 > 5:
            print('Error: p1 and p2 must be both in range [0 - 5]')
            exit(1)
        elif p2 < p1:
            print('Error: p2 must be smaller than p1')
            exit(1)
        crossover = crossover(p1,p2)
    
    elif config.crossover == 'anular':
        ap = crossover_params['ap']
        l = crossover_params['l']
        
        if ap is None:
            print("Error: Missing ap param at crossover")
            exit(1)
        elif l is None:
            print("Error: Missing l param at crossover")
            exit(1)
        elif not type(ap) == int or not type(l) == int:
            print('Error: ap and l must be integers')
            exit(1)
        ap = int(ap)
        l = int(l)
        if ap < 0 or ap > 5 or l < 0 or l > 3: #Pide que L e [0, Techo(S/2)]
            print('Error: ap and l must be both in range [0 - 5]')
            exit(1)
        
        crossover = crossover(ap,l)

    elif config.crossover == 'uniform':
        up = crossover_params['up']
        
        if up is None:
            print("Error: Missing up param at crossover")
            exit(1)
        elif not (type(up) == int or type(up) == float):
            print('Error: up must be an integer or a float')
            exit(1)
        up = int(up)
        if up < 0 or up > 1:
            print('Error: up must be in range [0 - 1]')
            exit(1)
        
        crossover = crossover(up)

    ## Mutation

    mutation = mutations.get(config.mutation, None)
    if mutation is None:
        print(f'Error: Crossover method "{config.mutation}" does not exist')
        exit(1)

    # they all needs params
    mutation_params = config.mutation_params

    if mutation_params is None:
        print("Error: Mutation params missing")
        exit(1)

    if config.mutation == 'gen':
        p = mutation_params['p']
        if p is None:
            print("Error: Missing p param at mutation")
            exit(1)
        elif not (type(p) == int or type(p) == float):
            print('Error: p must be a number')
            exit(1)
        p = float(p)
        if p <= 0:
            print('Error: p must be greater than 0')
            exit(1)

        mutation = mutation(p)
    else:
        mutation = mutation()

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

    # if needs params
    if config.stop == 'time' or config.stop == 'gens':
        stop_params = config.stop_params

        if stop_params is None:
            print("Error: Stop params missing")
            exit(1)

        if config.stop == 'time':
            max_time = stop_params['max_time']
            if max_time is None:
                print("Error: Missing max_time param at stop")
                exit(1)
            elif not (type(max_time) == int or type(max_time) == float):
                print('Error: max_time must be a number')
                exit(1)
            max_time = float(max_time)
            if max_time <= 0:
                print('Error: max_time must be greater than 0')
                exit(1)

            stop = stop(max_time)
        elif config.stop == 'gens':
            max_generations = stop_params['max_generation']
            if max_generations is None:
                print("Error: Missing max_generations param at stop")
                exit(1)
            elif not (type(max_generations) == int ) :
                print('Error: max_generations must be an integer')
                exit(1)
            max_generations = int(max_generations)
            if max_generations < 0:
                print('Error: max_generations must be greater than 0')
                exit(1)
            stop = stop(max_generations)

        elif config.stop == 'acceptable':
            mean_acceptable_fitness = stop_params['mean_acceptable_fitness']
            if mean_acceptable_fitness is None:
                print("Error: Missing mean_acceptable_fitness param at stop")
                exit(1)
            elif not (type(mean_acceptable_fitness) == int ) :
                print('Error: mean_acceptable_fitness must be an integer')
                exit(1)
            mean_acceptable_fitness = int(mean_acceptable_fitness)
            if mean_acceptable_fitness < 0:
                print('Error: mean_acceptable_fitness must be greater than 0')
                exit(1)
            stop = stop(mean_acceptable_fitness)
            

    else:
        stop = stop()

    # Initial population

    initial_population = config.initial_population
    if not type(initial_population) == int:
        print('Error: initial_population must be an integer')
        exit(1)
    if initial_population <= 0:
        print('Error: initial_population must be greater than 0')
        exit(1)

    # Items loading

    all_items = read_all_items(config.items_dataset_path, config.items_dataset_filenames)
    print("Items loaded")

    return Setup(all_items, crossover, mutation, K, A, B, method1, method2, method3, method4, implementation, stop, character_class_constructor, initial_population)