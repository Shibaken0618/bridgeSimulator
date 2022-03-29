
class Vector:
    def __init__(self,u,v):
        self.u = u
        self.v = v
    
    def __add__(self,other):
        new_u = self.u + other.u
        new_v = self.v + other.v
        return Vector(new_u, new_v)

    def __sub__(self,other):
        new_u = self.u - other.u
        new_v = self.v - other.v
        return Vector(new_u, new_v)