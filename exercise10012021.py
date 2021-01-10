#Definicja funkcji
# def dodaj(*args):
#   print(args)

# dodaj(2)
# dodaj(2,3)
# dodaj(3,4,5)
#############################
# def dodaj(*args):
#   wynik = 0
#   for arg in args:
#     wynik +=arg
#   return wynik

# # dodaj(2)
# # dodaj(2,3)
# dodaj(3,4,5)
####################
#Definicja funkcji z argumentami słownikowymi
#kontakenacja = łączenie
def konkatenacja(**kwargs):
  rezultat=""
  #print(kwargs)
  for kwargs in kwargs.values():
    rezultat += kwargs
    return rezultat
    
print(konkatenacja(pierwszy="hej", drugi=" ", trzeci="tam!"))

#konkatenacja(a="1")


###################

# for litera in "ala ma kota":
#   print(litera)



# lista = [1,2,3]

# for element in lista:
#   print(element)