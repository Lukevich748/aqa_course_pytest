import pytest
from calculator import Calculator

calc = Calculator()


class TestCalculator:

    @pytest.mark.parametrize(
        "a, b, expected", [
            (2, 2, 4),
            (-2, 8, 6),
            (11_423, 65_240, 76_663)
        ]
    )
    def test_sum(self, a, b, expected):
        assert calc.addition(a, b) == expected

    @pytest.mark.parametrize(
        "a, b, expected", [
            (10, 4, 6),
            (20_241, 10_000, 10_241),
            (-1435, 556, -1991)
        ]
    )
    def test_subtraction(self, a, b, expected):
        assert calc.subtraction(a, b) == expected

    @pytest.mark.parametrize(
        "a, b, expected", [
            (10, 2, 5),
            (2, 2, 1),
            (100, 32, 3.125)
        ]
    )
    def test_division(self, a, b, expected):
        assert calc.division(a, b) == expected

    @pytest.mark.parametrize(
        "a, b, expected", [
            (56, 7, 392),
            (2, 2, 4),
            (6, 6, 36)
        ]
    )
    def test_multiplication(self, a, b, expected):
        assert calc.multiplication(a, b) == expected
