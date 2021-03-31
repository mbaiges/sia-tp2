import signal
import sys
import multiprocessing as mp
import keyboard

from utils import read_config
from setup_builder import get_setup
from generators import get_initial_population
from plotters import plot_min_and_mean_fitness, plot_genetic_diversity, plot_best_ind_stats, plot_iterations_fitness, plot_all_iterations_fitnesses, plot_iterations_diversities
from stops import Generations

from models import Generation

print_rate_pctg = 0.1
print_rate = 100

fitness_plotter = None
diversity_plotter = None
best_ind_stats_plotter = None

def get_children(genes, char_gen):
    children = []

    for gene in genes:
        children.append(char_gen(gene))

    return children

def sigint_handler(sig, frame):
    print('Exiting')

    global fitness_plotter, diversity_plotter, best_ind_stats_plotter

    if not fitness_plotter is None:
        fitness_plotter.terminate()

    if not diversity_plotter is None:
        diversity_plotter.terminate()

    if not best_ind_stats_plotter is None:
        best_ind_stats_plotter.terminate()

    sys.exit(0)

def iterate(setup, multiple_times):
    generations = []

    initial_population = setup.initial_population

    # gen 0 - initial population
    initial_individuals = get_initial_population(setup.all_items, setup.character_class_constructor, initial_population)
    gen = Generation(initial_individuals, 0)
    gen_n = 0

    def select_A(individuals, gen_n, n):
        num = int(setup.A * n)
        ind1 = setup.method1.select(individuals, gen_n, num)
        ind2 = setup.method2.select(individuals, gen_n, n-num)
        return ind1 + ind2

    def select_B(individuals, gen_n, n):
        num = int(setup.B * n)
        ind1 = setup.method3.select(individuals, gen_n, num)
        ind2 = setup.method4.select(individuals, gen_n, n-num)
        return ind1 + ind2

    stop.ready()

    while not stop.reached_end(gen):
        generations.append(gen)

        if not multiple_times:
            fitness_plotter_q.put(gen)
            diversity_plotter_q.put(gen)
            best_ind_stats_plotter_q.put(gen)

            if config.stop == 'gens':
                max_gens = config.stop_params['max_generation']
                if gen_n % int(max_gens* print_rate_pctg) == 0:
                    print_percentage = int(100*gen_n/max_gens)
                    barr = '['
                    for i in range(0, int(print_percentage*print_rate_pctg)):
                        barr += '#'
                    for i in range(int(print_percentage*print_rate_pctg), int(100*print_rate_pctg)):
                        barr += ' '
                    barr += ']'
                    print(f'Iteration {gen_n}/{max_gens}: \t {barr} ({print_percentage}%)')
            elif gen_n % print_rate == 0:
                print("Iteration: ", gen_n)
        
        # select parents
        parents = select_A(gen.individuals, gen_n, setup.K)

        # crossover
        cross_gens = setup.crossover.cross(parents)

        # mutation
        mutated_gens = setup.mutation.mutate(cross_gens, setup)

        # children factory
        children = get_children(mutated_gens, setup.character_class_constructor)

        # implementation (fill all / fill parent)
        new_individuals = setup.implementation.fill(gen.individuals, children, gen_n, select_B)

        gen_n += 1
        gen = Generation(new_individuals, gen_n)

    return generations


def parse_results(setup, iterations):
    max_fitness_matrix = []
    avg_max_fitness = []
    mean_fitness_matrix = []
    avg_mean_fitness = []
    min_fitness_matrix = []
    avg_min_fitness = []
    diversity_matrix = []
    avg_diversity = []

    iteration_amnt = len(iterations)
    gen_size = len(iterations[0])

    for i in range(0, iteration_amnt):
        max_fitness_matrix.append([])
        mean_fitness_matrix.append([])
        min_fitness_matrix.append([])
        diversity_matrix.append([])
        
        for g in range(0, gen_size):           
            max_fitness_matrix[i].append(iterations[i][g].max_fitness())
            mean_fitness_matrix[i].append(iterations[i][g].mean_fitness())
            min_fitness_matrix[i].append(iterations[i][g].min_fitness())
            diversity_matrix[i].append(sum(iterations[i][g].genetic_diversity().values()))

    for g in range(0, gen_size) : 
        avg_max_fitness.append(0) 
        avg_mean_fitness.append(0) 
        avg_min_fitness.append(0)
        avg_diversity.append(0)
        for i in range(0, iteration_amnt):
            avg_max_fitness[g] += max_fitness_matrix[i][g]
            avg_mean_fitness[g] += mean_fitness_matrix[i][g]
            avg_min_fitness[g] += min_fitness_matrix[i][g]
            avg_diversity[g] += diversity_matrix[i][g]
        avg_max_fitness[g] /= iteration_amnt
        avg_mean_fitness[g] /= iteration_amnt 
        avg_min_fitness[g] /= iteration_amnt 
        avg_diversity[g] /= iteration_amnt

    plot_iterations_fitness(max_fitness_matrix, avg_max_fitness, f"Max fitnesses over {iteration_amnt} iterations and avg")
    plot_iterations_fitness(mean_fitness_matrix, avg_mean_fitness, f"Mean fitnesses over {iteration_amnt} iterations and avg")
    plot_iterations_fitness(min_fitness_matrix, avg_min_fitness, f"Min fitnesses over {iteration_amnt} iterations and avg")

    plot_all_iterations_fitnesses(max_fitness_matrix, mean_fitness_matrix, min_fitness_matrix, avg_max_fitness, avg_mean_fitness, avg_min_fitness, f"Max/Mean/Min fitnesses over {iteration_amnt} iterations and avg")

    plot_iterations_diversities(diversity_matrix, avg_diversity, f"Genetic diversity over {iteration_amnt} iterations and avg")

    return

if __name__ == '__main__':
    # sets SIGINT handler
    signal.signal(signal.SIGINT, sigint_handler)
   
    # sets process creation method
    mp.set_start_method('spawn')

    config = read_config()

    print(config)


    setup = get_setup(config)
    stop = setup.stop

    multiple_times = setup.multiple_times

    if not multiple_times:

        # https://docs.python.org/es/3.9/library/multiprocessing.html
        # multiprocessing
    
        fitness_plotter_q = mp.Queue()
        fitness_plotter_q.cancel_join_thread()
        diversity_plotter_q = mp.Queue()
        diversity_plotter_q.cancel_join_thread()
        best_ind_stats_plotter_q = mp.Queue()
        best_ind_stats_plotter_q.cancel_join_thread()
    
        fitness_plotter = mp.Process(target=plot_min_and_mean_fitness, args=((fitness_plotter_q),))
        fitness_plotter.daemon = True
        fitness_plotter.start()
    
        diversity_plotter = mp.Process(target=plot_genetic_diversity, args=((diversity_plotter_q),))
        diversity_plotter.daemon = True
        diversity_plotter.start()
    
        best_ind_stats_plotter = mp.Process(target=plot_best_ind_stats, args=((best_ind_stats_plotter_q),))
        best_ind_stats_plotter.daemon = True
        best_ind_stats_plotter.start()

        # # starts processing

        gens = iterate(setup, False)

        gen = gens[-1]

        fitness_plotter_q.put("STOP")
        diversity_plotter_q.put("STOP")
        best_ind_stats_plotter_q.put("STOP")

        print("Min fitness: ", gen.min_fitness())
        print("Mean fitness: ", gen.mean_fitness())
        print("Max fitness: ", gen.max_fitness()) 

    else:

        if not isinstance(setup.stop, Generations):
            print(setup.stop)
            print("Error: multiple times run is only available using stop: 'gens'")
            exit(1)

        iterations = []
        n = setup.multiple_times_iterations
        
        for i in range(0, n):
            iterations.append(iterate(setup, True))
            print(f"finished iteration {i}")

        print(f"parsing results...")
        parse_results(setup, iterations)

    print("End reached")

    print("Press 'q' to finish")

    keyboard.wait("q")


    # fitness_plotter.terminate()
    # diversity_plotter.terminate()
    # best_ind_stats_plotter.terminate()

    print("Exiting")

    exit(0)



