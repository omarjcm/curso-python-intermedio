'''
Crear un dictionary comprenhesion, un diccionario cuyas llaves sean los 1000 primeros numeros naturales con sus raices cuadradas como valores.
'''
def run():
    my_dict = {i: i**0.5 for i in range(1, 1001)}
    print(my_dict)


if __name__ == '__main__':
    run()