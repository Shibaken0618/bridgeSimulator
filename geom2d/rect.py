from geom2d.point import Point
from geom2d.size import Size

class Rect:
    def __init__(self, origin:Point, size:Size):
        self.origin = origin
        self.size = size

    @property
    def left(self):
        return self.origin.x

    @property
    def right(self):
        return self.origin.x + self.size.width

    @property
    def bottom(self):
        return self.origin.y

    @property
    def top(self):
        return self.origin.y + self.size.height

    @property
    def area(self):
        return self.size.width * self.size.height

    @property
    def perimeter(self):
        return 2 * self.size.width + 2 * self.size.height

    def contains_point(self, point:Point):
        return self.left < point.x < self.right \
            and self.bottom < point.y < self.top

    