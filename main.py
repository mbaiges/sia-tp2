from utils import read_config
from setup_builder import get_setup
from generators import get_initial_population

from models import Generation

def main():
    config = read_config()

    print(config)

    setup = get_setup(config)
    stop = setup.stop

    initial_population = setup.initial_population

    # gen 0 - initial population
    initial_individuals = get_initial_population(setup.all_items, setup.character_class_constructor, initial_population)
    gen = Generation(initial_individuals, 0)

    print(gen.individuals[0])

    stop.ready()

    # while not stop.reached_end(gen):
    #     print("Iterating")

    #     # select parents
    #     # parents1 = setup.method1.select(gen, setup.gen)

    #     # crossover
        

    #     # mutation

    #     # implementation (fill all / fill parent)

    print("End reached")


main()