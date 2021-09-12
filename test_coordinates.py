import pytest
from utils import coordinates_is_valid


def test_coordinates_valid():
    assert coordinates_is_valid("37.842762, 55.774558") == True


@pytest.mark.parametrize(
    "coordinates, expected",
    [
        ("37.842762, 55.774558", True),
        ("37.842789,55.76522", True),
        ("-73.985483,40.749200", True),
        ("40.749200,-73.985483", True),
        ("ashdmgf,-73.985483", False),
        ("123456,1234565",False),
        ('asdasdas,text is not valid', False)

    ]
)
def test_coordinates_valid_multi(coordinates, expected):
    assert coordinates_is_valid(coordinates) == expected
