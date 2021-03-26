

class FillAll:

    def __init__(self, fill_all_n):
        self.fill_all_n = fill_all_n
    

    def fill(self, parents, children, gen_n, selection_method):
        children_copy = children.copy()
        parents_selected = selection_method(parents, gen_n, self.fill_all_n)
        
        return children_copy + parents_selected



class FillParent:

    def __init__(self, fill_parent_n):
        self.fill_parent_n = fill_parent_n
    

    def fill(self, parents, children, gen_n, selection_method):
        child_amount = len(children)
        if self.fill_parent_n < child_amount :
            return selection_method(children, gen_n, self.fill_parent_n)
        else:
            children_copy = children.copy()
            parents_selected = selection_method(parents, gen_n, self.fill_all_n - child_amount)
            return children_copy + parents_selected
