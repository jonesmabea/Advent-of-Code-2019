import pytest
from day1.src.puzzle1 import calculate_fuel
from day1.src.puzzle2 import calculate_rec_fuel


@pytest.mark.parametrize("test_input,expected", [(12, 2), (14, 2), (1969,654), (100756,33583)])
def test_calculate_fuel(test_input, expected):
    assert calculate_fuel(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [(12, 2), (1969, 966), (100756, 50346)])
def test_calculate_rec_fuel(test_input, expected):
    assert calculate_rec_fuel(test_input) == expected