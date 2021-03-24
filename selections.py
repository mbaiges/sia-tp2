class Elite:

    def select(self, gen, K):

        def key_f(ind):
            return ind.fitness

        sorted_individuals = sorted(gen.individuals, key=key_f, reverse=True)

        N = len(sorted_individuals)

        selected = []
        selected_n = 0

        i = 0
        while selected_n < K:
            n = int(math.ceil((K - i)/N))
            while n > 0 and selected_n < K:
                selected.append(sorted_individuals[i])
                selected_n += 1
                n -= 0
            i += 1

        return selected

class Roulette:

    def select(self, gen, K):
        return 0
