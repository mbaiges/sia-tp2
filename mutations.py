import random
import numpy as np

from constants import min_height, max_height
from generators import get_rand_item

# gen = [height, items.weapon, items.boots, items.helmet, items.gloves, items.breastplate] 

def get_random_height(all_items):
    return random.uniform(min_height, max_height)

def get_random_weapon(all_items):
    return get_rand_item(all_items.weapons)

def get_random_boots(all_items):
    return get_rand_item(all_items.boots)

def get_random_helmet(all_items):
    return get_rand_item(all_items.helmets)

def get_random_gloves(all_items):
    return get_rand_item(all_items.gloves)

def get_random_breastlate(all_items):
    return get_rand_item(all_items.breastplates)

def mutate_gen(gene_to_mutate, all_items):

    switcher = {
        0: get_random_height,
        1: get_random_weapon,
        2: get_random_boots,
        3: get_random_helmet,
        4: get_random_gloves,
        5: get_random_breastlate
    }

    func = switcher.get(gene_to_mutate, None)

    if func is None:
        print("Error: Mutate switch off bounds")
        exit(1)
    else:
        return func(all_items)


class Gen:

    def __init__(self, p):
        self.p = p

    def mutate(self, genes, setup):
        
        for gene in genes:
            mutation_chance = random.uniform(0, 1)
            if mutation_chance < self.p:
                gene_to_mutate = random.randint(0,len(gene)-1)
                gene[gene_to_mutate] = mutate_gen(gene_to_mutate, setup.all_items)

        return genes

class MultigenLimitada:
    
    def __init__(self, p):
        self.p = p

    def mutate(self, genes, setup):

        for gene in genes:
            mutation_chance = random.uniform(0, 1)
            if mutation_chance < self.p:
                genes_amount = len(gene)
                amount_of_genes_to_mutate = random.randint(1,genes_amount)
                rand_indexes = [random.randint(0, genes_amount-1) for a in range(0, amount_of_genes_to_mutate)]
                #rand_indexes = np.random.randint(0,genes_amount-1,amount_of_genes_to_mutate)
                for i in rand_indexes:
                    gene[i] = mutate_gen(i, setup.all_items)

        return genes

class MultigenUniforme:
    
    def __init__(self, p):
        self.p = p

    def mutate(self, genes, setup):

        for gene in genes:
            for i in range(0,len(gene)-1):
                mutation_chance = random.uniform(0, 1)
                if mutation_chance < self.p:
                    gene[i] = mutate_gen(i, setup.all_items)

        return genes

class Completa:
    
    def __init__(self, p):
        self.p = p
    
    def mutate(self, genes, setup):
        for gene in genes:
            mutation_chance = random.uniform(0, 1)
            if mutation_chance < self.p:
                for i in range(0,len(gene)-1):
                    gene[i] = mutate_gen(i, setup.all_items)

        return genes

