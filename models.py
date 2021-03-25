import math

class ItemsFilenames:

    def __init__(self, weapons_filename, boots_filename, helmets_filename, gloves_filename, breastplates_filename):
        self.weapons = weapons_filename
        self.boots = boots_filename
        self.helmets = helmets_filename
        self.gloves = gloves_filename
        self.breastplates = breastplates_filename

class Config:

    def __init__(self, crossover, crossover_params, mutation, mutation_params, K, A, B, method1, method1_params, method2, method2_params, method3, method3_params, method4, method4_params, implementation, stop, stop_params, items_dataset_path, weapons_filename, boots_filename, helmets_filename, gloves_filename, breastplates_filename, character_class, initial_population):
        self.crossover = crossover
        self.crossover_params = crossover_params
        self.mutation = mutation
        self.mutation_params = mutation_params
        self.K = K
        self.A = A
        self.B = B
        self.method1 = method1
        self.method1_params = method1_params
        self.method2 = method2
        self.method2_params = method2_params
        self.method3 = method3
        self.method3_params = method3_params
        self.method4 = method4
        self.method4_params = method4_params
        self.implementation = implementation
        self.stop = stop
        self.stop_params = stop_params
        self.items_dataset_path = items_dataset_path
        self.items_dataset_filenames = ItemsFilenames(weapons_filename, boots_filename, helmets_filename, gloves_filename, breastplates_filename)
        self.character_class = character_class
        self.initial_population = initial_population

    def __str__(self):
        s = 'Config:\n'
        s += f'\tcrossover: {self.crossover}\n'
        s += f'\t\tcrossover_params: {self.crossover_params}\n'
        s += f'\tmutation: {self.mutation}\n'
        s += f'\t\tmutation_params: {self.mutation_params}\n'
        s += f'\tselection:\n'
        s += f'\t\tK: {self.K}\n'
        s += f'\t\tA: {self.A}\n'
        s += f'\t\tB: {self.B}\n'
        s += f'\t\tmethod1: {self.method1}\n'
        s += f'\t\t\tmethod1_params: {self.method1_params}\n'
        s += f'\t\tmethod2: {self.method2}\n'
        s += f'\t\t\tmethod2_params: {self.method2_params}\n'
        s += f'\t\tmethod3: {self.method3}\n'
        s += f'\t\t\tmethod3_params: {self.method3_params}\n'
        s += f'\t\tmethod4: {self.method4}\n'
        s += f'\t\t\tmethod4_params: {self.method4_params}\n'
        s += f'\timplementation: {self.implementation}\n'
        s += f'\tstop: {self.stop}\n'
        s += f'\t\tstop_params: {self.stop_params}\n'
        s += f'\titems_dataset:\n'
        s += f'\t\tpath: {self.items_dataset_path}\n'
        s += f'\t\tweapons: {self.items_dataset_filenames.weapons}\n'
        s += f'\t\tboots: {self.items_dataset_filenames.boots}\n'
        s += f'\t\thelmets: {self.items_dataset_filenames.helmets}\n'
        s += f'\t\tgloves: {self.items_dataset_filenames.gloves}\n'
        s += f'\t\tbreastplates: {self.items_dataset_filenames.breastplates}\n'
        s += f'\tcharacter_class: {self.character_class}\n'
        s += f'\tinitial_population: {self.initial_population}'
        return s

class Item:

    def __init__(self, idx, ident, strength, agility, expertise, resistance, life):
        self.idx = idx
        self.id = ident
        self.strength = strength
        self.agility = agility
        self.expertise = expertise
        self.resistance = resistance
        self.life = life

class Weapon(Item):

    def __init__(self, idx, ident, strength, agility, expertise, resistance, life):
        super().__init__(idx, ident, strength, agility, expertise, resistance, life)

class Boots(Item):

    def __init__(self, idx, ident, strength, agility, expertise, resistance, life):
        super().__init__(idx, ident, strength, agility, expertise, resistance, life)

class Helmet(Item):

    def __init__(self, idx, ident, strength, agility, expertise, resistance, life):
        super().__init__(idx, ident, strength, agility, expertise, resistance, life)

class Gloves(Item):

    def __init__(self, idx, ident, strength, agility, expertise, resistance, life):
        super().__init__(idx, ident, strength, agility, expertise, resistance, life)

class Breastplate(Item):

    def __init__(self, idx, ident, strength, agility, expertise, resistance, life):
        super().__init__(idx, ident, strength, agility, expertise, resistance, life)

class ItemsSet:

    def __init__(self, weapon, boots, helmet, gloves, breastplate):
        self.weapon = weapon
        self.boots = boots
        self.helmet = helmet
        self.gloves = gloves
        self.breastplate = breastplate

    def list_items(self):
        return [self.weapon, self.boots, self.helmet, self.gloves, self.breastplate]

class AllItems:
    
    def __init__(self, weapons, boots, helmets, gloves, breastplates):
        self.weapons = weapons
        self.boots = boots
        self.helmets = helmets
        self.gloves = gloves
        self.breastplates = breastplates

class Character:

    def __init__(self, gens): # items es un ItemsSet
        height = gens[0]
        items = ItemsSet(gens[1], gens[2], gens[3], gens[4], gens[5])

        self.items = items

        items_strength = 0
        items_agility = 0
        items_expertise = 0
        items_resistance = 0
        items_life = 0

        for item in items.list_items():
            items_strength += item.strength
            items_agility += item.agility
            items_expertise += item.expertise
            items_resistance += item.resistance
            items_life += item.life

        self.strength = 100 * math.tanh(0.01 * items_strength)
        self.agility = math.tanh(0.01 * items_agility)
        self.expertise = 0.6 * math.tanh(0.01 * items_expertise)
        self.resistance = math.tanh(0.01 * items_resistance)
        self.life = 100 * math.tanh(0.01 * items_life)

        # height must be [1.3m - 2.0m]
        self.height = height

        self.gens = [self.height, self.items.weapon, self.items.boots, self.items.helmet, self.items.gloves, self.items.breastplate]

        self.ATM = 0.7 - (3*self.height - 5)**4 + (3*self.height - 5)**2 + self.height/4.0
        self.DEM = 1.9 + (2.5*self.height - 4.16)**4 - (2.5*self.height - 4.16)**2 - 3*self.height/10.0

        self.attack = (self.agility + self.expertise) * self.strength * self.ATM
        self.defense = (self.resistance + self.expertise) * self.life * self.DEM

    def __str__(self):
        s = 'Character:\n'
        s += '\tStats:\n'
        s += f'\t\tstrength: {self.strength}\n'
        s += f'\t\tagility: {self.agility}\n'
        s += f'\t\texpertise: {self.expertise}\n'
        s += f'\t\tresistance: {self.resistance}\n'
        s += f'\t\tlife: {self.life}\n'
        s += f'\tHeight: {self.height}\n'
        s += '\tModifiers:\n'
        s += f'\t\tAttack (ATM): {self.ATM}\n'
        s += f'\t\tDefense (DEM): {self.DEM}\n'
        s += f'\tAttack: {self.attack}\n'
        s += f'\tDefense: {self.defense}'
        return s

class Warrior(Character):

    def __init__(self, gens):
        super().__init__(gens)
        self.fitness = 0.6 * self.attack + 0.6 * self.defense

    def __str__(self):
        s = super().__str__()
        s += '\n\tClass: Warrior\n'
        s += f'\tFitness: {self.fitness}'
        return s

class Archer(Character):

    def __init__(self, gens):
        super().__init__(gens)
        self.fitness = 0.9 * self.attack + 0.1 * self.defense

    def __str__(self):
        s = super().__str__()
        s += '\n\tClass: Archer\n'
        s += f'\tFitness: {self.fitness}'
        return s

class Defender(Character):

    def __init__(self, gens):
        super().__init__(gens)
        self.fitness = 0.3 * self.attack + 0.8 * self.defense

    def __str__(self):
        s = super().__str__()
        s += '\n\tClass: Defender\n'
        s += f'\tFitness: {self.fitness}'
        return s

class Infiltrate(Character):

    def __init__(self, gens):
        super().__init__(gens)
        self.fitness = 0.8 * self.attack + 0.3 * self.defense

    def __str__(self):
        s = super().__str__()
        s += '\n\tClass: Infiltrate\n'
        s += f'\tFitness: {self.fitness}'
        return s

class Setup:

    def __init__(self, all_items, crossover, mutation, K, A, B, method1, method2, method3, method4, implementation, stop, character_class_constructor, initial_population):
        self.all_items = all_items
        self.crossover = crossover
        self.mutation = mutation
        self.K = K
        self.A = A
        self.B = B
        self.method1 = method1
        self.method2 = method2
        self.method3 = method3
        self.method4 = method4
        self.implementation = implementation
        self.stop = stop
        self.character_class_constructor = character_class_constructor
        self.initial_population = initial_population

class Generation:

    def __init__(self, individuals, number):
        self.individuals = individuals
        self.number = number

    def min_fitness(self):
        res = math.inf
        for ind in self.individuals:
            if ind.fitness < res:
                res = ind.fitness
        return res

    def mean_fitness(self):
        res = 0
        for ind in self.individuals:
            res += ind.fitness
        return res / len(self.individuals) 