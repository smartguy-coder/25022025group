import pytest

from utils import add_two_numbers


class TestAddTwoNumbers:
    def test_add_two_numbers_success(self):
        number1 = 2
        number2 = 3
        expected_result = 5
        actual_result = add_two_numbers(number1, number2)
        assert actual_result == expected_result, "fix add_two_numbers"

    def test_add_two_strings_success(self):
        number1 = "23"
        number2 = "23"
        expected_result = 46
        actual_result = add_two_numbers(number1, number2)
        assert actual_result == expected_result

    def test_add_two_strings_fail(self):
        number1 = "dfgjhdfg"
        number2 = "ljkdfghkjdfg"
        with pytest.raises(ValueError):
            add_two_numbers(number1, number2)
