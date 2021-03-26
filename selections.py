import random
import math

class Elite:

    def select(self, individuals, gen_n, K):

        def key_f(ind):
            return ind.fitness

        sorted_individuals = sorted(individuals, key=key_f, reverse=True)

        N = len(sorted_individuals)

        selected = []
        selected_n = 0

        i = 0
        while selected_n < K:
            n = int(math.ceil((K - i)/N))
            while n > 0 and selected_n < K:
                selected.append(sorted_individuals[i])
                selected_n += 1
                n -= 1
            i += 1

        return selected

class Roulette:

    def select(self, individuals, gen_n, K):
        
        total_fitness = 0

        for ind in individuals:
            total_fitness += ind.fitness

        mapped_individuals = []
        acum = 0

        for ind in individuals:
            rel = ind.fitness / total_fitness
            acum += rel
            mapped_individuals.append((ind, rel, acum))

        selected = []
        selected_n = 0

        while selected_n < K:
            rj = random.uniform(0, 1)

            i = 0
            while rj > mapped_individuals[i][2]:
                i += 1

            selected.append(mapped_individuals[i][0])
            selected_n += 1

        return selected

class Universal:

    def select(self, individuals, gen_n, K):
        
        total_fitness = 0

        for ind in individuals:
            total_fitness += ind.fitness

        mapped_individuals = []
        acum = 0

        for ind in individuals:
            rel = ind.fitness / total_fitness
            acum += rel
            mapped_individuals.append((ind, rel, acum))

        selected = []
        selected_n = 0

        while selected_n < K:
            r = random.uniform(0, 1)

            rj = (r + selected_n)/K

            i = 0
            while rj > mapped_individuals[i][2]:
                i += 1

            selected.append(mapped_individuals[i][0])
            selected_n += 1

        return selected

class Boltzmann:

    def __init__(self, initial_temp, min_temp, k):
        self.initial_temp = initial_temp
        self.min_temp = min_temp
        self.k = k

    def select(self, individuals, gen_n, K):

        avg_exp_fi_t = 0

        for ind in individuals:
            avg_exp_fi_t += self._exp_fi_t(ind, self._temperature(gen_n))

        avg_exp_fi_t /= len(individuals)

        total_pseudo_fitness = 0

        for ind in individuals:
            total_pseudo_fitness += (self._exp_fi_t(ind, self._temperature(gen_n))/avg_exp_fi_t)

        mapped_individuals = []
        acum = 0

        for ind in individuals:
            rel = (self._exp_fi_t(ind, self._temperature(gen.n))/avg_exp_fi_t) / total_pseudo_fitness
            acum += rel
            mapped_individuals.append((ind, rel, acum))

        selected = []
        selected_n = 0

        while selected_n < K:
            rj = random.uniform(0, 1)

            i = 0
            while rj > mapped_individuals[i][2]:
                i += 1

            selected.append(mapped_individuals[i][0])
            selected_n += 1

        return selected

    def _exp_fi_t(self, ind, temp):
        return math.exp(ind.fitness/temp)

    def _temperature(self, n):
        return self.min_temp + (self.initial_temp - self.min_temp)*math.exp(-k*n)