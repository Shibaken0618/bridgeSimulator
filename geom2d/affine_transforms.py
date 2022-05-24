import math
from geom2d.affine_transf import AffineTransform
from geom2d.point import Point

def make_scale(sx:float, sy:float, center=Point(0,0)):
    return AffineTransform(
        sx = sx,
        sy = sy,
        tx = center.x * (1.0 - sx),
        ty = center.y * (1.0 - sy)
    )

def make_rotation(radians:float, center = Point(0,0)):
    cos = math.cos(radians)
    sin = math.sin(radians)
    one_minus_cos = 1.0 - cos
    return AffineTransform(
        sx=cos,
        sy=cos,
        tx=center.x * one_minus_cos + center.y * sin,
        ty=center.y * one_minus_cos - center.x * sin,
        shx=-sin,
        shy=sin
    )