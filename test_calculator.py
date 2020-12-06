import unittest

from calculator import calculate

class TestCalculator(unittest.TestCase):
  def test_dodawanie(self):
    r = calculate(1, 2, '+')
    self.assertEqual(r, 3)
  def test_odejmowanie(self):
    r = calculate(10, 120, "-")
    self.assertEqual(r, -110)