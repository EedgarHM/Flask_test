import pytest
from utils import calc_coordinates


def test_calc_coordinates():
    assert calc_coordinates((55.759357, 37.612605), (40.749200, -73.985483)) == "7527 KM"


@pytest.mark.parametrize(
    "coordinate_a, coordinate_b, expected",
    [
        ((55.759357, 37.612605), (61.672533,50.836237), "1008 KM")


    ]
)
def test_calc_coordinates_multi(coordinate_a, coordinate_b, expected):
    assert calc_coordinates(coordinate_a, coordinate_b) == expected
