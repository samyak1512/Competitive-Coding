class Multiset:

    def __init__(self):
        self.l = []

    def add(self, val):
        # adds one occurrence of val from the multiset, if any
        pass        #('pass' is a nothing operation. When it execute, nothing happens.)
        return self.l.append(val)

    def remove(self, val):
        # removes one occurrence of val from the multiset, if any
        pass
        if val in self.l:
            return  self.l.remove(val)
    
    def __contains__(self, val):
        # returns True when val is in the multiset, else returns False
        if val in self.l:
            return True
        else:
            return False

    def __len__(self):
        # returns the number of elements in the multiset
        return len(self.l)
