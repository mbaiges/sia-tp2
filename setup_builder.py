from models import Warrior, Archer, Defender, Infiltrate, Setup
from selections import Elite, Roulette, Universal, Boltzmann, DeterministicTournaments, ProbabilisticTournaments, Ranking
from crossovers import OnePoint, TwoPoints, Anular, Uniform
from mutations import Gen, MultigenLimitada, MultigenUniforme, Completa
from stops import Time, Generations, Acceptable, Struct, Content
from implementations import FillAll, FillParent

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
    'gen': Gen,
    'multi_limited': MultigenLimitada,
    'multi_uniform': MultigenUniforme,
    'full': Completa
}

selections = {
    'elite': Elite,
    'roulette': Roulette,
    'universal': Universal,
    'boltzmann': Boltzmann,
    'det_tournaments': DeterministicTournaments,
    'prob_tournaments': ProbabilisticTournaments,
    'ranking': Ranking
}

implementations = {
    'fill_all': FillAll,
    'fill_parent': FillParent
}

stops = {
    'time': Time,
    'gens': Generations,
    'acceptable': Acceptable,
    'struct': Struct,
    'content': Content
}


def get_selection(name, params, initial_population):
    method = selections.get(name, None)
    if method is None:
        print(f'Error: Selection method 1 "{name}" does not exist')
        exit(1)

    # if needs params
    if name == 'boltzmann' or name == 'prob_tournaments' or name == 'det_tournaments':

        if params is None:
            print(f'Error: {name} params missing')
            exit(1)

        if name == 'boltzmann':
            min_temp = params['min_temp']
            if min_temp is None:
                print(f'Error: Missing min_temp param at {name}')
                exit(1)
            elif not (type(min_temp) == int or type(min_temp) == float):
                print('Error: min_temp must be a number')
                exit(1)
            min_temp = float(min_temp)
            if min_temp <= 0:
                print('Error: min_temp must be greater than 0')
                exit(1)

            initial_temp = params['initial_temp']
            if initial_temp is None:
                print(f'Error: Missing initial_temp param at {name}')
                exit(1)
            elif not (type(initial_temp) == int or type(initial_temp) == float):
                print('Error: initial_temp must be a number')
                exit(1)
            initial_temp = float(initial_temp)
            if initial_temp <= min_temp:
                print('Error: initial_temp must be greater than min_temp')
                exit(1)

            k = params['k']
            if k is None:
                print(f'Error: Missing k param at {name}')
                exit(1)
            elif not (type(k) == int or type(k) == float):
                print('Error: k must be a number')
                exit(1)
            k = float(k)
            if k <= 0:
                print('Error: k must be greater than 0')
                exit(1)

            return method(initial_temp, min_temp, k)
        elif name == 'det_tournaments':
            m = params['m']
            
            if m is None:
                print(f'Error: Missing m param at {name}')
                exit(1)
            elif not type(m) == int:
                print('Error: m must be an integer')
                exit(1)
            m = int(m)
            if m < 1 or m >= initial_population:
                print(f'Error: m must be in range [1 - {initial_population-1}]')
                exit(1)

            return method(m)
        elif name == 'prob_tournaments':
            pt_threshold = params['pt_threshold']
            
            if pt_threshold is None:
                print(f'Error: Missing pt_threshold param at {name}')
                exit(1)
            elif not (type(pt_threshold) == int or type(pt_threshold) == float):
                print('Error: pt_threshold must be an integer or a float')
                exit(1)
            pt_threshold = float(pt_threshold)
            if pt_threshold < 0.5 or pt_threshold > 1:
                print('Error: pt_threshold must be in range [0.5 - 1]')
                exit(1)

            return method(pt_threshold)
    else:
        return method()

def get_setup(config):

    # Character class

    character_class_constructor = characters_classes.get(config.character_class, None)

    if character_class_constructor is None:
        print(f'Error: Character class "{config.character_class}" does not exist')
        exit(1)

    # Initial population

    initial_population = config.initial_population
    if not type(initial_population) == int:
        print('Error: initial_population must be an integer')
        exit(1)
    if initial_population <= 0:
        print('Error: initial_population must be greater than 0')
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

    method1 = get_selection(config.method1, config.method1_params, initial_population)
    
        ## Method 2

    method2 = get_selection(config.method2, config.method2_params, initial_population)

    ## Method 3

    method3 = get_selection(config.method3, config.method3_params, initial_population)


    ## Method 4

    method4 = get_selection(config.method4, config.method4_params, initial_population)


    # Genetic operators

    ## Crossover --------------------------------------------------------------------------------------------------------------------------

    crossover = crossovers.get(config.crossover, None)
    if crossover is None:
        print(f'Error: Crossover method "{config.crossover}" does not exist')
        exit(1)

    ## if need params
    if config.crossover == 'anular' or config.crossover == 'uniform':

        crossover_params = config.crossover_params
        if crossover_params is None:
            print("Error: Crossover params missing")
            exit(1)

        elif config.crossover == 'anular':
            l = crossover_params['l']
            
            if l is None:
                print("Error: Missing l param at crossover")
                exit(1)
            elif not type(l) == int:
                print('Error: l must be integer')
                exit(1)
            l = int(l)
            if l < 0 or l > 3: #Pide que L e [0, Techo(S/2)]
                print('Error: l must be in range [0 - 3]')
                exit(1)
            
            crossover = crossover(l)

        elif config.crossover == 'uniform':
            p = crossover_params['p']
            
            if p is None:
                print("Error: Missing p param at crossover")
                exit(1)
            elif not (type(p) == int or type(p) == float):
                print('Error: p must be an integer or a float')
                exit(1)
            p = float(p)
            if p < 0 or p > 1:
                print('Error: p must be in range [0 - 1]')
                exit(1)
            
            crossover = crossover(p)
    else:
        crossover = crossover()

    ## Mutation ---------------------------------------------------------------------------------

    mutation = mutations.get(config.mutation, None)
    if mutation is None:
        print(f'Error: Mutation method "{config.mutation}" does not exist')
        exit(1)

    # they all needs params
    mutation_params = config.mutation_params

    if mutation_params is None:
        print("Error: Mutation params missing")
        exit(1)

    if config.mutation == 'gen':
        pg = mutation_params['pg']
        if pg is None:
            print("Error: Missing pg param at mutation")
            exit(1)
        elif not (type(pg) == int or type(pg) == float):
            print('Error: pg must be a number')
            exit(1)
        pg = float(pg)
        if pg < 0 or pg > 1:
            print('Error: pg must be between 0 and 1')
            exit(1)
        mutation = mutation(pg)
    elif config.mutation == 'multi_limited':
        pml = mutation_params['pml']
        if pml is None:
            print("Error: Missing pml param at mutation")
            exit(1)
        elif not (type(pml) == int or type(pml) == float):
            print('Error: pg must be a number')
            exit(1)
        pml = float(pml)
        if pml < 0 or pml > 1:
            print('Error: pml must be between 0 and 1')
            exit(1)
        mutation = mutation(pml)
    elif config.mutation == 'multi_uniform':
        pmu = mutation_params['pmu']
        if pmu is None:
            print("Error: Missing pmu param at mutation")
            exit(1)
        elif not (type(pmu) == int or type(pmu) == float):
            print('Error: pg must be a number')
            exit(1)
        pmu = float(pmu)
        if pmu < 0 or pmu > 1:
            print('Error: pg must be between 0 and 1')
            exit(1)
        mutation = mutation(pmu)
    elif config.mutation == 'full':
        pf = mutation_params['pf']
        if pf is None:
            print("Error: Missing pf param at mutation")
            exit(1)
        elif not (type(pf) == int or type(pf) == float):
            print('Error: pf must be a number')
            exit(1)
        pf = float(pf)
        if pf < 0 or pf > 1:
            print('Error: pf must be between 0 and 1')
            exit(1)
        mutation = mutation(pf)

    # Implementation-----------------------------------------------------------------------------

    implementation = implementations.get(config.implementation, None)
    if implementation is None:
        print(f'Error: Implementation method "{config.implementation}" does not exist')
        exit(1)

    implementation = implementation(initial_population)
    
    # Stop -------------------------------------------------------------

    stop = stops.get(config.stop, None)
    if stop is None:
        print(f'Error: Stop method "{config.stop}" does not exist')
        exit(1)

    # if needs params
 
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
    
    elif config.stop == 'struct':
        relevant_percentage_of_change = stop_params['relevant_percentage_of_change']
        if relevant_percentage_of_change is None:
            print("Error: Missing relevant_percentage_of_change param at stop")
            exit(1)
        elif not (type(relevant_percentage_of_change) == int or type(relevant_percentage_of_change) == float):
            print('Error: relevant_percentage_of_change must be a number')
            exit(1)
        relevant_percentage_of_change = float(relevant_percentage_of_change)
        if relevant_percentage_of_change < 0 or relevant_percentage_of_change > 1:
            print('Error: relevant_percentage_of_change must be between [0.0 - 1.0]')
            exit(1)

        considered_gens = stop_params['considered_gens']
        if considered_gens is None:
            print("Error: Missing considered_gens param at stop")
            exit(1)
        elif not type(considered_gens) == int:
            print('Error: considered_gens must be a number')
            exit(1)
        considered_gens = int(considered_gens)
        if considered_gens < 0:
            print('Error: considered_gens must be greater than 0')
            exit(1)

        stop = stop(relevant_percentage_of_change, considered_gens)
    
    elif config.stop == 'content':
        max_generations_counter = stop_params['max_generations_counter']
        if max_generations_counter is None:
            print("Error: Missing max_generations_counter param at stop")
            exit(1)
        elif not (type(max_generations_counter) == int ) :
            print('Error: max_generations_counter must be an integer')
            exit(1)
        max_generations_counter = int(max_generations_counter)
        if max_generations_counter < 0:
            print('Error: max_generations_counter must be greater than 0')
            exit(1)
        stop = stop(max_generations_counter)

    # Items loading

    all_items = read_all_items(config.items_dataset_path, config.items_dataset_filenames)
    print("Items loaded")

    # Multiple times

    multiple_times = config.multiple_times
    multiple_times_iterations = config.multiple_times_iterations

    if multiple_times:
        if multiple_times_iterations is None:
            print("Error: Missing iterations param at multiple_times")
            exit(1)
        elif not (type(multiple_times_iterations) == int ) :
            print('Error: iterations must be an integer')
            exit(1)
        multiple_times_iterations = int(multiple_times_iterations)
        if multiple_times_iterations < 0:
            print('Error: iterations must be greater than 0')
            exit(1)

    return Setup(all_items, crossover, mutation, K, A, B, method1, method2, method3, method4, implementation, stop, character_class_constructor, initial_population, multiple_times, multiple_times_iterations)