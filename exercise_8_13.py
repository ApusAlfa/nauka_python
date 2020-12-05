print('exercise 8 plus 13!')
zwierz_1 = {'nazwa': 'Pan kot',
            'wiek': '3',
            'rasa': 'mieszana'}
zwierz_2 = {'nazwa': 'Pani kot',
            'wiek': '5',
            'rasa': 'mieszana ruda'}

zoo = [zwierz_1, zwierz_2]

#print(zoo[0])
#print(zoo[1])


for z in zoo:
    print(z)

#for z in range(len(zoo)):
#    print("z:" + str(z) + ":" zoo{z)

#for a, b in zoo.items():
#    print("{0}:{1}".format(a, b))

for a in zwierz_1:
    print("{0}:{1}".format(a, zwierz_1[a]))

for a, b in zwierz_2.items():
    print("{0}:{1}".format(a, b))
