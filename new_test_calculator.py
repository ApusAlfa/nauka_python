import unittest

from new_calculator import str_calculate

class TestCalculator(unittest.TestCase):
  def test_dodawanie(self):
    r = str_calculate(1, 2, 'concat')
    self.assertEqual(r, 3)
    print('Obecna wartosc dodawania: ' + str(r))