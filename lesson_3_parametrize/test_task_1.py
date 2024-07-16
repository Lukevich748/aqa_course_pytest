import pytest


class TestSum:

    @pytest.mark.parametrize(
        "a, b, expected", [
            (1, 4, 5),
            (-1, -4, -5),
            (0, 100, 100),
            (10_000, 1488, 11_488),
            (-456, 785, 329)
        ]
    )
    def test_sum_numbers(self, a, b, expected):
        result = a + b
        assert result == expected, f"Expected {expected}, but got {result}."
