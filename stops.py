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
        return gen.number >= max_generations


class Acceptable:
    
    def __init__(self, mean_acceptable_fitness):
        self.mean_acceptable_fitness = mean_acceptable_fitness
    
    def ready(self):
        return

    def reached_end(self, gen):
        return gen.mean_fitness() >= mean_acceptable_fitness


