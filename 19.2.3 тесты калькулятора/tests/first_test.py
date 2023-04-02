
import pytest
from app.Calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 2,2) == 4

    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 2, 2) == 1

    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 2, 2) == 0

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 2, 2) == 4