def print_dict(dict):
    for key in dict:
        print("{0}:{1}".format(key, d[key]))

if __name__ == "__main__":
    samolot = {'name': 'boeing', 'przebieg': 10000, 'type': 'pasazerski'}

    print_dict(samolot)

    samolot['dlugosc'] = 10.5
    print_dict(samolot)
