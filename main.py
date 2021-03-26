import signal
import sys

from utils import read_config
from setup_builder import get_setup
from generators import get_initial_population

from models import Generation

def get_children(genes, char_gen):
    children = []

    for gene in genes:
        children.append(char_gen(gene))

    return children

def sigint_handler(sig, frame):
    print('Exiting')
    sys.exit(0)

def main():

    signal.signal(signal.SIGINT, sigint_handler)

    config = read_config()

    print(config)

    setup = get_setup(config)
    stop = setup.stop

    initial_population = setup.initial_population

    # gen 0 - initial population
    initial_individuals = get_initial_population(setup.all_items, setup.character_class_constructor, initial_population)
    gen = Generation(initial_individuals, 0)
    gen_n = 0

    def select_A(individuals, gen_n, n):
        num = int(setup.A * n)
        print("n_A = ", n)
        print("num_A: ", num)
        ind1 = setup.method1.select(individuals, gen_n, num)
        ind2 = setup.method2.select(individuals, gen_n, 1-num)
        return ind1 + ind2

    def select_B(individuals, gen_n, n):
        num = int(setup.B * n)
        print("n_B = ", n)
        print("num_B: ", num)
        ind1 = setup.method3.select(individuals, gen_n, num)
        ind2 = setup.method4.select(individuals, gen_n, 1-num)
        return ind1 + ind2

    print("First population")
    print(gen.individuals)

    stop.ready()

    while not stop.reached_end(gen):
        print("Iteration number: ", gen_n)
        print("Number of individuals: ", len(gen.individuals))
        
        # select parents

        parents = select_A(gen.individuals, gen_n, setup.K)

        # print("Parents in iteration:", parents)

        # print(parents)

        # crossover
        
        cross_gens = setup.crossover.cross(parents)
        # print("Crossover done!")
        # print(cross_gens)

        # mutation

        mutated_gens = setup.mutation.mutate(cross_gens, setup)
        # print("Mutation done!")
        # print(mutated_gens)

        # children factory
        children = get_children(mutated_gens, setup.character_class_constructor)
        #print("Oh! Look at the baby boy !")
        #print(children[0])

        # implementation (fill all / fill parent)

        new_individuals = setup.implementation.fill(gen.individuals, children, gen_n, select_B)

        gen_n += 1
        gen = Generation(new_individuals, gen_n)

    ## end of while

    print(gen.individuals[0])

    print("End reached")


main()