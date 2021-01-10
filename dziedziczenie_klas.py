# Definicja klasy
class Czlowiek():
    gatunek = "homo sapiens"
    # Metoda inicjalizacyjna - jest automatycznie wywoływana
    # W momencie inicjalizacji obiektu
    def __init__(self, imie):
        print("Tworzymy człowieka o imieniu ", imie)
        self.imie = imie
    def introduce_your(self):
        print("Cześć, jestem ", self.imie, "i jestem gatunku ", self.gatunek)


#Definicja klasy pochodnej
class Dziecko(Czlowiek):
  def introduce_your(self):
    print("Cześć, wszystkim!")
    super(.introduce_your) # Wywoływanie metody dziedziczonej po człowieku a nie po dziecku

  def baw_sie(self):
    print("Ale zabawa, juhhuu!")


# Tworzenie obiektów (instancji klasy Czlowiek)
adam=Czlowiek('Adam') #self to adam -> adam.imie = "Adam"
ewa=Czlowiek('Ewa') #self to ewa -> ewa.imie = "Ewa"

# adam.introduce_your()
# print(adam.imie)
# print(adam.gatunek)

kain=Dziecko("Kain")
ewa.introduce_your()
kain.introduce_your()
#kain.baw_sie()

# Wywoływanie metody dziedziczonej po człowieku a nie po dziecku

kain=Dziecko("Kain")
ewa.introduce_your()
kain.introduce_your()