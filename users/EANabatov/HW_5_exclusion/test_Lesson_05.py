import pytest

from Functions_Lesson_05 import search_by_name
from Functions_Lesson_05 import safe_divide
from Functions_Lesson_05 import interactive_calculator


# noinspection PyTypeChecker
class TestSearchByName:
    def test_basic_work(self):
        """basic work testing"""
        assert search_by_name("Alex") == 89153566547

    def test_key_error(self):
        """basic exception testing"""
        assert search_by_name("Keks") == str("Такого имени нет")

    def test_lower_case_name(self):
        """testing lower case name"""
        assert search_by_name("alex") == 89153566547

    def test_upper_case_name(self):
        """testing upper case name"""
        assert search_by_name("ALEX") == 89153566547

    def test_lower_and_upper_case_name(self):
        """testing the input of the first lowercase letter and the uppercase of the others"""
        assert search_by_name("aLEX") == 89153566547

    def test_input_int_number(self):
        """testing input int number"""
        assert search_by_name(666) == str(
            "Некорректный тип данных, принимаются только строки")

    def test_input_float_number(self):
        """ testing input float number """
        assert search_by_name(666.666) == str(
            "Некорректный тип данных, принимаются только строки")

    def test_input_complex_number(self):
        """testing input complex number"""
        assert search_by_name(666 + 0j) == str(
            "Некорректный тип данных, принимаются только строки")

    def test_input_list(self):
        """testing input list"""
        assert search_by_name([666]) == str(
            "Некорректный тип данных, принимаются только строки")

    def test_input_dictionary(self):
        """testing input dictionary"""
        assert search_by_name({1: 666}) == str(
            "Некорректный тип данных, принимаются только строки")

    def test_input_boolean(self):
        """testing input boolean"""
        assert search_by_name(True) == str(
            "Некорректный тип данных, принимаются только строки")

    def test_input_sets(self):
        """testing input sets"""
        assert search_by_name({666, True, 666.666}) == str(
            "Некорректный тип данных, принимаются только строки")


# noinspection PyTypeChecker
class TestSafeDivide:
    def test_normal_work(self):
        """Testing basic program function with int numbers on input"""
        assert safe_divide(20, 5) == str("4.000")

    def test_float_dividend(self):
        """Testing basic program function with float dividend and int divider on input"""
        assert safe_divide(20.5, 5) == str("4.100")

    def test_float_divider(self):
        """Testing basic program function with int dividend and float divider on input"""
        assert safe_divide(20, 5.5) == str("3.636")

    def test_float_dividend_and_divider(self):
        """Testing basic program function with float numbers on input"""
        assert safe_divide(20.5, 5.5) == str("3.727")

    def test_complex_input(self):
        """Testing basic program function with complex numbers on input"""
        assert safe_divide(666 + 0j, 333 + 0j) == str("2.000+0.000j")

    def test_zero_division_error(self):
        """Testing ZeroDivisionError with zero divider on input"""
        assert safe_divide(20, 0) == str("На ноль делить нельзя")

    def test_input_list_and_zero_division_error(self):
        """Testing TypeError with list dividend and zero divider on input"""
        assert safe_divide([666], 0) == str("Некорректный тип данных, принимаются только числа")

    def test_input_dictionary(self):
        """Testing TypeError with dictionary on input"""
        assert safe_divide({1: 666}, {1: 666}) == str("Некорректный тип данных, принимаются только числа")

    def test_dictionary_zero_division_error(self):
        """Testing TypeError with dictionary dividend and zero divider on input"""
        assert safe_divide({1: 666}, 0) == str("Некорректный тип данных, принимаются только числа")

    def test_input_boolean(self):
        """Testing input boolean (1 / 1)"""
        assert safe_divide(True, True) == str("1.000")

    def test_input_boolean_and_zero_division_error(self):
        """Testing input boolean and check ZeroDivisionError (1 / 0)"""
        assert safe_divide(True, False) == str("На ноль делить нельзя")

    def test_input_sets(self):
        """Testing TypeError with sets on input"""
        assert safe_divide({666, True, 666.666}, {666, True, 666.666}) == str("Некорректный тип данных, принимаются "
                                                                              "только числа")


# noinspection PyTypeChecker
class TestInteractiveCalculator:
    def test_basic_work_addition(self):
        """Testing basic addition function of program"""
        assert interactive_calculator("3 + 2") == 5

    def test_basic_work_subtraction(self):
        """Testing basic subtraction function of program"""
        assert interactive_calculator("3 - 2") == 1

    def test_basic_work_multiplication(self):
        """Testing basic multiplication function of program"""
        assert interactive_calculator("3 * 2") == 6

    def test_basic_work_division(self):
        """Testing basic division function of program"""
        assert interactive_calculator("3 / 2") == 1.5

    def test_input_int(self):
        """Testing AttributeError with int on input"""
        assert interactive_calculator(2 + 0) == str("Принимается только строка!")

    def test_input_float(self):
        """Testing AttributeError with float on input"""
        assert interactive_calculator(2.0 + 0) == str("Принимается только строка!")

    def test_input_float_in_string(self):
        """Testing ValueError with float dividend and zero divider on input"""
        assert interactive_calculator("2.0 / 0") == str("Необходимо ввести целые числа!")

    def test_zero_division_error(self):
        """Testing ZeroDivisionError with int dividend and zero divider"""
        assert interactive_calculator("2 / 0") == str("На ноль делить нельзя!")
