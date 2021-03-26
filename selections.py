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

class DeterministicTournaments:

    def select(self, individuals, gen_n, K):
        selected = []
        selected_n = 0

        while selected_n < K:
            idx1 = random.randint(0, len(individuals) - 1)
            idx2 = random.randint(0, len(individuals) - 1)

            ind1 = individuals[idx1]
            ind2 = individuals[idx2]

            if ind1.fitness >= ind2.fitness:
                chosen = ind1
            else:
                chosen = ind2

            selected.append(chosen)
            selected_n += 1

        return selected

class ProbabilisticTournaments:

    def __init__(self, threshold):
        self.threshold = threshold

    def select(self, individuals, gen_n, K):
        selected = []
        selected_n = 0

        while selected_n < K:
            idx1 = random.randint(0, len(individuals) - 1)
            idx2 = random.randint(0, len(individuals) - 1)

            ind1 = individuals[idx1]
            ind2 = individuals[idx2]

            r = random.uniform(0, 1)

            # if r < self.threshold:
            #     if ind1.fitness >= ind2.fitness:
            #         chosen = ind1
            #     else:
            #         chosen = ind2
            # else:
            #     if ind1.fitness >= ind2.fitness:
            #         chosen = ind2
            #     else:
            #         chosen = ind1

            # refactored
            if (r < self.threshold and ind1.fitness >= ind2.fitness) or (ind1.fitness < ind2.fitness):
                chosen = ind1
            else:
                chosen = ind2

            selected.append(chosen)
            selected_n += 1

        return selected

class Ranking:

    def select(self, individuals, gen_n, K):

        mp_inds = []

        for ind in individuals:
            mp_inds.append([ind, 0])

        def key_f(mp_ind):
            return mp_ind[0].fitness

        sorted_mp_inds = sorted(mp_inds, key=key_f, reverse=True)

        N = len(sorted_mp_inds)

        def pseudo_fitness(rank_idx):
            return (1.0*(N - rank_idx))/N 
        
        total_pseudo_fitness = 0

        for i in range(0, len(sorted_mp_inds)):
            sorted_mp_inds[i][1] = pseudo_fitness(i)
            total_pseudo_fitness += pseudo_fitness(i)

        print(mp_inds)

        mapped_individuals = []
        acum = 0

        for mp_ind in mp_inds:
            rel = mp_ind[1] / total_pseudo_fitness
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

