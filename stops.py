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


# class Struct: #TODO
#     current_generation = None
#     def __init__(self, relevant_percentage_of_change):
#         self.relevant_percentage_of_change = relevant_percentage_of_change
    
#     def ready(self):
#         return

#     def reached_end(self, gen):
#         if  current_generation is None:
#             current_generation = gen
#             return False

#         if 
#         return gen.mean_fitness() >= mean_acceptable_fitness


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
            if generations_counter == max_generations_counter:
                return True
            return False

        current_max_fitness = max_fit
        generations_counter = 0
        return False

