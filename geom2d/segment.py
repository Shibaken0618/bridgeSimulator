from geom2d.point import Point
from geom2d.vectors import make_vector_between, make_versor_between
from geom2d import tparam

class Segment:

    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    @property
    def direction_vector(self):
        return make_vector_between(self.start, self.end)

    @property
    def direction_versor(self):
        return make_versor_between(self.start, self.end)

    @property
    def normal_versor(self):
        return self.direction_versor.perpendicular()

    @property
    def length(self):
        return self.start.distance_to(self.end)

    def point_at(self, t:float):
        tparam.ensure_valid(t)
        return self.start.displaced(self.direction_vector,t)

    @property
    def middle(self):
        return self.point_at(tparam.MIDDLE)

    def closest_point_to(self, p:Point):
        v = make_vector_between(self.start, p)
        d = self.direction_versor
        vs = v.projection_over(d)
        if vs < 0:
            return self.start
        if vs > self.length:
            return self.end
        return self.start.displaced(d,vs)

    