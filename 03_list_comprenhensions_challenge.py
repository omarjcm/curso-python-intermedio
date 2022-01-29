'''
Reto: Crear un list comprenhension, una lista de todos los multiplos de 4 que a la vez tambien son multiplos de 6 y 9, hasta 5 digitos.
'''
def run():
    my_list = [i for i in range(1, 100000) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]
    print(my_list)


if __name__ == '__main__':
    run()