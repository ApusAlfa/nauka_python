import unittest

from calculator import calculate

class TestCalculator(unittest.TestCase):
  def test_dodawanie(self):
    r = calculate(1, 2, '+')
    self.assertEqual(r, 3)
  def test_odejmowanie(self):
    r = calculate(10, 120, "-")
    self.assertEqual(r, -110)
  def test_mnozenie(self):
    rm = calculate(4, 6, "*")
    self.assertEqual(rm, 24)
  def test_dzielenie(self):
    rd = calculate(6, 3, "/")
    self.assertEqual(rd, 2)
  def test_procent(self):
    pr = calculate(6, 100, "%")
    self.assertEqual(pr, 0.06)
  def test_potega(self):
    po = calculate(3, 2, "^")
    self.assertEqual(po, 9)