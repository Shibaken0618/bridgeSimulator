import unittest

from geom2d.point import Point
from geom2d.polygon import Polygon
from geom2d.rect import Rect
from geom2d.size import Size

class TestRect(unittest.TestCase):
    origin = Point(0,0)
    size = Size(10,5)
    rect = Rect(origin, size)

    def test_contains_point(self):
        point = Point(5,3)
        self.assertTrue(self.rect.contains_point(point))

    def test_doesnt_contain_point(self):
        point = Point(50,7)
        self.assertFalse(self.rect.contains_point(point))

    