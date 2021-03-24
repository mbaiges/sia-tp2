import random

class OnePoint:

    def __init__(self, p):
        self.p = p

    def cross(parents, setup):
        
        # Los parent vienen así [[p1, p2], [p3, p4], ......]
        
        children = []

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
            children.append(setup.character_class(cgen1))
            children.append(setup.character_class(cgen2))
        
        return children                



class TwoPoints:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def cross(parents, setup):

        children = []

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
            children.append(setup.character_class(cgen1))
            children.append(setup.character_class(cgen2))
        
        return children        

class Anular: 

    def __init__(self, p, l):
        self.p = p
        self.l = l

    def cross(parents, setup):

        children = []

        for ppair in parents:
            i = 0 
            cgen1 = []
            cgen2 = []
            size = len(ppair[0].gens)
            while i < size:
                if (i > p and i < p+l) or (((p+l) % size < p) and i < ((p+l) % size)): 
                    cgen1.append(ppair[1].gens[i])
                    cgen2.append(ppair[0].gens[i])
                else:
                    cgen1.append(ppair[0].gens[i])
                    cgen2.append(ppair[1].gens[i])
                i += 1

            children.append(setup.character_class(cgen1))
            children.append(setup.character_class(cgen2))
        
        return children        



class Uniform:

    def __init__(self, p):
        self.p = p

    def cross(parents, setup):
        
        # Los parent vienen así [[p1, p2], [p3, p4], ......]
        
        children = []

        for ppair in parents:
            i = 0 
            cgen1 = []
            cgen2 = []
            while i < len(ppair[0].gens):
                randnum = random.uniform(0, 1)
                if randnum < p:
                    cgen1.append(ppair[0].gens[i])
                    cgen2.append(ppair[1].gens[i])
                else:
                    cgen1.append(ppair[1].gens[i])
                    cgen2.append(ppair[0].gens[i])
                i += 1
            children.append(setup.character_class(cgen1))
            children.append(setup.character_class(cgen2))
        
        return children                

