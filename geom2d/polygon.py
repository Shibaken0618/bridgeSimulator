from pip import List
from geom2d.point import Point
from geom2d.segment import Segment
from utils.pairs import make_round_pairs
import operator
from functools import reduce

class Polygon:
    def __init__(self, vertices: List[Point]):
        if len(vertices) < 3:
            raise ValueError('Need 3 or more vertices')
        self.vertices = vertices

    def sides(self):
        vertex_pairs = make_round_pairs(self.vertices)
        return [
            Segment(pair[0], pair[1])
            for pair in vertex_pairs
        ]

    @property
    def centroid(self):
        vtx_count = len(self.vertices)
        vtx_sum = reduce(operator.add, self.vertices)
        return Point(
            vtx_sum.x / vtx_count,
            vtx_sum.y / vtx_count
        )