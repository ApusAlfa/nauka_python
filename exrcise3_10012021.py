#Klasy, własne obiekty o typach danych
# a=4
# print(type(a))
# print(dir(int))
# print(dir(a)) #- pokaże metody wewnątrz klasy a
# #directory - dir() chcę zobaczyć co jest w klasie, sprawdzam zawartość
# bool(a) #python skorzysta z magic method __bool__

#Programowanie wysokopoziomowe/obiektowe
# #Definicja klasy
# class Czlowiek():
#   gatunek = "homo sapiens"

# #Tworzenie obiektów (instancji klasy Czlowiek)
# adam=Czlowiek()
# ewa=Czlowiek()

# print(adam.gatunek)
# print(ewa.gatunek)

# adam.imie = "Adam"
# print(adam.imie)
# print(ewa.imie)
######################################
#Definicja klasy
class Czlowiek():
  gatunek = "homo sapiens"
  # Metoda inicjalizacyjna - jest automatycznuie wywoływana
  # W momencie inicjalizacji obiektu
  def __init__(self, imie):
    #print("Inicjalizacja instancji klasy Człowiek")
    print("Tworzymy człowieka o imieniu", imie)
    self.imie = imie
    
#Tworzenie obiektów (instancji klasy Czlowiek)
adam=Czlowiek('Adam') #adam.imie="Adam"
ewa=Czlowiek('Ewa') #ewa.imie="Ewa"

#print(dir(ewa))
