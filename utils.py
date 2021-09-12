import re
from geopy.distance import geodesic as g
from math import floor, ceil


def coordinates_is_valid(coordinates):
    """
        Funcion que evalua si las coordenadas ingresadas son validas
        :param coordinates:
        :return: true o false if the coordinates is valid
    """
    is_valid = (re.search(
        "^[-+]?([1-8]?\d(\.\d+)?|90(\.0+)?),\s*[-+]?(180(\.0+)?|((1[0-7]\d)|([1-9]?\d))(\.\d+)?)$", coordinates))

    if is_valid:
        return True
    else:
        return False


def calc_coordinates(coordinate_a, coordinate_b):
    """
        funcion que calcula la distancia entre el ring road
        y un punto cualquiera

        :param coordinate_a:
        :param coordinate_b:
        :return: distance beetwen coordinate_a and coordinate_b
    """
    calc_km = str(g(coordinate_a, coordinate_b).km)
    result = float(calc_km[:9])
    return f"{ceil(result)} KM"
