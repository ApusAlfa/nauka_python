import unittest

from new_calculator import str_calculate

class TestCalculator(unittest.TestCase):
  def test_dodawanie(self):
    r = str_calculate(1, 2, 'concat')
    self.assertEqual(r, 3)
    print('Obecna wartosc dodawania: ' + str(r))

class TestStringCalculator(unittest.TestCase):
  def test_concat(self):
    r = str_calculate("a", "b", 'concat')
    self.assertEqual(r, 'ab')
    print('Obecna wartosc ab: ' + str(r))

  def test_awb1(self):
    r = str_calculate("a", "b", "awb")
    self.assertEqual(r, False)

  def test_awb2(self):
    r = str_calculate("a", "bab", "awb")
    self.assertEqual(r, True)

  def test_last1(self):
    r = str_calculate("a", "ba", "last_sign_in_b_shbe_a")
    self.assertEqual(r, True)
    print(r)
  
  def test_last2(self):
    r = str_calculate("aba", "b", "last_sign_in_a_shbe_b")
    self.assertEqual(r, True)
    print(r)

