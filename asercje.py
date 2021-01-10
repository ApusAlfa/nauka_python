import unittest
#SZABLON
# #Asercje
# #"Czysty" Python
# assert 3 > 4

class MojPrzypadekTestowy(unittest.TestCase):
  #Przygotowanie do testu
  #(Analogia: Warunki wstępne)
  def setUp(self):
    #pass
    print("setUp")

  #Sprzątanie po teście
  def tearDown(self):
    #pass
    print(tearDown)

  #Metoda testowa (musi zaczynać się od słowa "test")
  def testPierwszy(self):
    #pass
    #Czysty Python
    assert 1 == 1
    # To samo przy wykorzystaniu unittesta
    self.assertEqual(1,1)
    # Przykład
    #self.assertEqual(komunikat, "Zły email") porównuje komunikat z tym na stronie.

###################

  def testDrugi(self):
    pass


if __name__ == "__main__":
  unittest.main(verbosity=2)
