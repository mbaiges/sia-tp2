from utils import read_config
from setup_builder import get_setup
from generators import get_initial_population

from models import Generation

def get_children(genes, char_gen):
    children = []

    for gene in genes:
        children.append(char_gen(gene))

    return children


def main():
    config = read_config()

    print(config)

    setup = get_setup(config)
    stop = setup.stop

    initial_population = setup.initial_population

    # gen 0 - initial population
    initial_individuals = get_initial_population(setup.all_items, setup.character_class_constructor, initial_population)
    gen = Generation(initial_individuals, 0)
    gen_n = 0

    def select_A(gen, n):
        num = int(setup.A * n)
        ind1 = setup.method1.select(gen, num)
        ind2 = setup.method2.select(gen, 1-num)
        return ind1 + ind2

    def select_B(gen, n):
        num = int(setup.B * n)
        ind1 = setup.method3.select(gen, num)
        ind2 = setup.method4.select(gen, 1-num)
        return ind1 + ind2

    print("First population")
    print(gen.individuals)

    stop.ready()

    while not stop.reached_end(gen):
        print("Iteration number: ", gen_n)
        
        # select parents

        parents = select_A(gen, K)

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

        new_individuals = setup.fill.fill(gen.individuals, children, select)

        gen_n += 1

        return
    ## end of while

    print("End reached")


main()