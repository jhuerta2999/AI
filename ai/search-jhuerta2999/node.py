class Node:
    def __init__(self, name, g, h, p, pg):
        self.name = name
        self.costToReach = g + pg
        self.costFrom = h
        self.estimatedTotal = self.costFrom + self.costToReach
        self.parent = p
        
    def __lt__(self, other):
        if self.name[0] < other.name[0]:
            return True
        else:
            return False
