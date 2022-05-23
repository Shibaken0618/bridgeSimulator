from geom2d.point import Point
from geom2d.segment import Segment
from geom2d.polygon import Polygon
from geom2d.rect import Rect
from geom2d.circle import Circle

class AffineTransform:
    def __init__(self, sx=1, sy=1, tx=0, ty=0, shx=0, shy=1):
        self.sx = sx
        self.sy = sy
        self.tx = tx
        self.ty = ty
        self.shx = shx
        self.shy = shy

    def apply_to_point(self, point:Point):
        return Point(
            (self.sx * point.x) + (self.shx*point.y) + self.tx,
            (self.shy * point.x) + (self.sy * point.y) + self.ty
        )

    def apply_to_segment(self, segment:Segment):
        return Segment(
            self.apply_to_point(segment.start),
            self.apply_to_point(segment.end)
        )

    def apply_to_polygon(self, polygon:Polygon):
        return Polygon(
            [self.apply_to_point(v) for v in polygon.vertices]
        )

    def apply_to_rect(self, rect:Rect):
        return self.apply_to_polygon(
            rect.to_polygon()
        )

    def apply_to_circle(self, circle:Circle, divisions=30):
        return self.apply_to_polygon(
            circle.to_polygon(divisions)
        )

    