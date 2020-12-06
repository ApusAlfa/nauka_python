haslo = input("Podaj haslo: ")
if len(haslo) < 3:
  print("Haslo jest za krotkie")
else:
  ilosc_gwiazdek = len(haslo[1:-1])
  gwiazdy = ilosc_gwiazdek * "*"
  print(haslo[0] + gwiazdy +haslo[-1])