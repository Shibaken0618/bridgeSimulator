import re
import json
from geom2d import Point
import pkg_resources as res


def parse_points():
    return (
        __point_from_string(input()),
        __point_from_string(input()),
        __point_from_string(input()),
    )


def __point_from_string(string: str):
    matches = re.match(r'(?P<x>\d+)\s(?P<y>\d+)', string)
    return Point(
        int(matches.group('x')),
        int(matches.group('y'))
    )


def read_config():
    config = res.resource_string(__name__, 'config.json')
    return json.loads(config)
