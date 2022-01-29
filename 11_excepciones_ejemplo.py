def divisors(num):
    try:
        if num < 0:
            raise ValueError('Los numeros a ingresar deben ser positivos.')
        divisors = []
        for i in range(1, num + 1):
            if num % i == 0:
                divisors.append(i)
        return divisors
    except ValueError as error:
        print( error )

def run():
    try:
        num = int(input('Ingresa un número: '))
        print(divisors(num))
        print("Terminó mi programa")
    except ValueError:
        print('Debes ingresar un numero.')


if __name__ == '__main__':
    run()