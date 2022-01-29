print('---------------------------Ejercicio 1') 

def palindrome(cadena):
    return cadena == cadena[::-1]

try:
    print(palindrome(2))
except TypeError:
    print('Solo se pueden ingresar cadenas de caracteres.')

print('---------------------------Ejercicio 2') 

def palindrome2(cadena):
    try:
        if (len(cadena) == 0):
            raise ValueError('No se puede ingresar una cadena vacia.')
        return cadena == cadena[::-1]
    except ValueError as error:
        print(error)
        return False

try:
    print(palindrome(2))
except TypeError:
    print('Solo se pueden ingresar cadenas de caracteres.')
finally:
    print(palindrome2(''))

