from datetime import datetime

class Time:

    def __init__(self, max_time):
        self.max_time = max_time

    def ready(self):
        self.start_time = datetime.now()

    def reached_end(self, gen):
        try:
            return (datetime.now() - self.start_time).total_seconds() >= self.max_time
        except:
            print("Error: Ready hasn't been called")
            return True


class Generations:
    
    def __init__(self, max_generations):
        self.max_generations = max_generations
    
    def ready(self):
        return

    def reached_end(self, gen):
        return gen.number >= self.max_generations




class Acceptable:
    
    def __init__(self, mean_acceptable_fitness):
        self.mean_acceptable_fitness = mean_acceptable_fitness
    
    def ready(self):
        return

    def reached_end(self, gen):
        return gen.mean_fitness() >= self.mean_acceptable_fitness


class Struct:
    
    def __init__(self, relevant_percentage_of_change, considered_gens):
        self.relevant_percentage_of_change = relevant_percentage_of_change
        self.considered_gens = considered_gens
        self.bags = []
    
    def ready(self):
        return

    def reached_end(self, gen):
        # print(f"Gen N {gen.number} - Bags recorded: {len(self.bags)}")

        if len(self.bags) < self.considered_gens:
            self.bags.append(gen.genetic_diversity_bag())
            return False
        elif len(self.bags) == self.considered_gens:
            self.bags.pop(0)
            self.bags.append(gen.genetic_diversity_bag())

        int_bag = {}

        for bag in self.bags:
            for t, amount in bag.items():
                int_bag[t] = amount

        for i in range(0, len(self.bags) - 1):
            bag = self.bags[i]
            for t, amount in bag.items():
                if t in int_bag and amount < int_bag[t]:
                    int_bag[t] = amount
            
            for t in int_bag.copy():
                if t not in bag:
                    int_bag.pop(t)

        values = int_bag.values()

        unchanged = 0

        if values:
            unchanged = sum(values)

        # print(f"Similarity: {(unchanged / len(gen.individuals) * 1.0)}")

        return (unchanged / len(gen.individuals) * 1.0) >= self.relevant_percentage_of_change


class Content:

    current_max_fitness = 0
    generations_counter = 0

    def __init__(self, max_generations_counter):
        self.max_generations_counter = max_generations_counter
    
    def ready(self):
        return

    def reached_end(self, gen): #TODO: Seguir pa
        max_fit = gen.max_fitness()
        if current_max_fitness == max_fit:
            generations_counter += 1
            if generations_counter == self.max_generations_counter:
                return True
            return False

        current_max_fitness = max_fit
        generations_counter = 0
        return False

