

class FillAll:

    def __init__(self, N):
        self.N = N
    
    def fill(self, parents, children, gen_n, selection_method):
        return selection_method(parents + children, gen_n, self.N)

class FillParent:

    def __init__(self, N):
        self.N = N
    
    def fill(self, parents, children, gen_n, selection_method):
        child_amount = len(children)
        if child_amount < self.N:
            return children + selection_method(parents, gen_n, self.N - child_amount)
        else:
            return selection_method(children, gen_n, self.N)
