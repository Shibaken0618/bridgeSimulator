import unittest

from geom2d.point import Point
from geom2d.polygon import Polygon
from geom2d.segment import Segment

class TestPolygon(unittest.TestCase):
    vertices = [
        Point(0,0),
        Point(30,0),
        Point(0,30),
    ]
    polygon = Polygon(vertices)

    def test_slides(self):
        expected = [
            Segment(self.vertices[0], self.vertices[1]),
            Segment(self.vertices[1], self.vertices[2]),
            Segment(self.vertices[2], self.vertices[0])
        ]
        actual = self.polygon.sides()
        self.assertEqual(expected,actual)

    def test_centroid(self):
        expected = Point(10,10)
        actual = self.polygon.centroid
        self.assertEqual(expected,actual)
