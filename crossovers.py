import random


# p1 p2 p3 p4 p5 p6 p7
# p1 p2 p3 p4 p5 p6

def pair_parents(parents):
    i = 0
    pparents = []

    if(len(parents) == 1 or len(parents) == 0):
        print('Error: pair_parents must have more than 1 parent')
        exit(1)

    while i < len(parents):
        if i == len(parents) - 1 : 
            pparents.append([parents[i-1], parents[i]])
        else:
            pparents.append([parents[i], parents[i+1]])
        i += 2

    return pparents


class OnePoint:

    def cross(self, parents):
        p = random.randint(0, 5)
        parents = pair_parents(parents)
        # Los parent vienen así [[p1, p2], [p3, p4], ......]
        
        children_gens = []

        for ppair in parents:
            i = 0 
            cgen1 = []
            cgen2 = []
            while i < p:
                cgen1.append(ppair[0].gens[i])
                cgen2.append(ppair[1].gens[i])
                i += 1
            while i < len(ppair[0].gens):
                cgen1.append(ppair[1].gens[i])
                cgen2.append(ppair[0].gens[i])
                i += 1
            children_gens.append(cgen1)
            children_gens.append(cgen2)
        
        return children_gens                



class TwoPoints:

    def cross(self, parents):
        p1 = random.randint(0, 5)
        p2 = random.randint(p1, 5)
        
        parents = pair_parents(parents)

        children_gens = []

        for ppair in parents:
            i = 0 
            cgen1 = []
            cgen2 = []
            while i < p1:
                cgen1.append(ppair[0].gens[i])
                cgen2.append(ppair[1].gens[i])
                i += 1
            while i < p2:
                cgen1.append(ppair[1].gens[i])
                cgen2.append(ppair[0].gens[i])
                i += 1
            while i < len(ppair[0].gens):
                cgen1.append(ppair[0].gens[i])
                cgen2.append(ppair[1].gens[i])
                i += 1
            children_gens.append(cgen1)
            children_gens.append(cgen2)
        
        return children_gens        

class Anular: 

    def __init__(self, l):
        self.l = l

    def cross(self, parents):
        p = random.randint(0, 4)
        
        parents = pair_parents(parents)
        children_gens = []

        for ppair in parents:
            i = 0 
            cgen1 = []
            cgen2 = []
            size = len(ppair[0].gens)
            while i < size:
                if (i > p and i < p+self.l) or (((p+self.l) % size < p) and i < ((p+self.l) % size)): 
                    cgen1.append(ppair[1].gens[i])
                    cgen2.append(ppair[0].gens[i])
                else:
                    cgen1.append(ppair[0].gens[i])
                    cgen2.append(ppair[1].gens[i])
                i += 1

            children_gens.append(cgen1)
            children_gens.append(cgen2)
        
        return children_gens        



class Uniform:

    def __init__(self, p):
        self.p = p

    def cross(self, parents):
        
        parents = pair_parents(parents)
        # Los parent vienen así [[p1, p2], [p3, p4], ......]
        
        children_gens = []

        for ppair in parents:
            i = 0 
            cgen1 = []
            cgen2 = []
            while i < len(ppair[0].gens):
                randnum = random.uniform(0, 1)
                if randnum < self.p:
                    cgen1.append(ppair[0].gens[i])
                    cgen2.append(ppair[1].gens[i])
                else:
                    cgen1.append(ppair[1].gens[i])
                    cgen2.append(ppair[0].gens[i])
                i += 1
            children_gens.append(cgen1)
            children_gens.append(cgen2)
        
        return children_gens                
 

