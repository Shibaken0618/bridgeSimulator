from typing import List
from geom2d import Point, Segment, Rect, Circle, Polygon, Vector
from graphic.svg.attributes import attrs_to_str
from graphic.svg.read import read_template

__segment_template = read_template('line.txt')
__rect_template = read_template('rect.txt')
__circle_template = read_template('circle.txt')
__polygon_template = read_template('polygon.txt')
__polyline_template = read_template('polyline.txt')
__text_template = read_template('text.txt')
__group_template = read_template('group.txt')

def segment(seg: Segment, attributes=()):
    return __segment_template \
        .replace('{{x1}}', str(seg.start.x)) \
        .replace('{{y1}}', str(seg.start.y)) \
        .replace('{{x2}}', str(seg.end.x)) \
        .replace('{{y2}}', str(seg.end.y)) \
        .replace('{{attrs}}', attrs_to_str(attributes))

def rectangle(rect: Rect, attributes=()):
    return __rect_template \
        .replace('{{x}}', str(rect.origin.x)) \
        .replace('{{y}}', str(rect.origin.y)) \
        .replace('{{width}}', str(rect.size.width)) \
        .replace('{{height}}', str(rect.size.height)) \
        .replace('{{attrs}}', attrs_to_str(attributes))

def circle(circ: Circle, attributes=()):
    return __circle_template \
        .replace('{{cx}}', str(circ.center.x)) \
        .replace('{{cy}}', str(circ.center.y)) \
        .replace('{{r}}', str(circ.radius)) \
        .replace('{{attrs}}', attrs_to_str(attributes))

def polygon(pol: Polygon, attributes=()):
    return __polygon_template \
        .replace('{{points}}', __format_points(pol.vertices)) \
        .replace('{{attrs}}', attrs_to_str(attributes))

def __format_points(points: List[Point]):
    return ' '.join([f'{p.x},{p.y}' for p in points])

def polyline(points: List[Point], attributes=()):
    return __polyline_template \
        .replace('{{points}}', __format_points(points)) \
        .replace('{{attrs}}', attrs_to_str(attributes))

def text(txt: str, pos: Point, disp: Vector, attrs_list=()):
    return __text_template \
        .replace('{{x}}', str(pos.x)) \
        .replace('{{y}}', str(pos.y)) \
        .replace('{{dx}}', str(disp.u)) \
        .replace('{{dy}}', str(disp.v)) \
        .replace('{{text}}', txt) \
        .replace('{{attrs}}', attrs_to_str(attrs_list))

def group(primitives: List[str], attributes=()):
    return __group_template \
        .replace('{{content}}', '\n'.join(primitives)) \
        .replace('{{attrs}}', attrs_to_str(attributes))

def arrow(
    _segment: Segment,
    length: float,
    height: float,
    attributes=()):

    director = _segment.direction_vector
    v_1 = director.opposite().with_length(length)
    v_h1 = director.perpendicular().with_length(height/2.0)
    v_h2 = v_h1.opposite()
    return group(
        [
            segment(_segment),
            polyline([
                _segment.end.displaced(v_1 + v_h1),
                _segment.end,
                _segment.end.displaced(v_1 + v_h2)
            ])
        ],
        attributes
    )