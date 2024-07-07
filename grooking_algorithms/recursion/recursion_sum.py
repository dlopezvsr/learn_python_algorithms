lista = [2, 4, 5, 7, 8, 4, 3, 6, 8]
lista2 = [1]

def sumar(array):
    if not array:
        return 0
    return array[0] + sumar(array[1:])


