import math
from geom2d.vector import Vector

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def distance_to(self,other):
        delta_x = other.x - self.x
        delta_y = other.y - self.y
        return math.sqrt(delta_x**2 + delta_y**2)


    def __add__(self,other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x,new_y)

    def __sub__(self,other):
        new_x = self.x - other.x
        new_y = self.y - other.y
        return Vector(new_x,new_y)



# p = Point(1,3)
# q = Point(2,4)

# print((q-p).__dict__)
# print((p+q).__dict__)