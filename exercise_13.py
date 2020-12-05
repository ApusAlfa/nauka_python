print('zadanie13!')

zwierz = {'nazwa': 'Pan kot',
            'wiek': '3',
            'rasa': 'mieszana'}

print(zwierz['nazwa'])
print(zwierz['wiek'])


#print(zwierz['masc'])
print(zwierz.get('masc'))
print('#############')

for a in zwierz:
    print("{0}:{1}".format(a, zwierz[a]))

print('#############')

for a, b in zwierz.items():
    print("{0}:{1}".format(a, b))
