from utils import read_config
from setup_builder import get_setup

def main():
    config = read_config()

    print(config)

    setup = get_setup(config)
    stop = setup.stop

    initial_population = setup.initial_population

    # gen 0 - initial population

    stop.ready()

    gen = 'Soy la generacion 0'

    while not stop.reached_end(gen):
        print("Iterating")

        # select parents

        # crossover

        # mutation

        # implementation (fill all / fill parent)

    print("End reached")


main()