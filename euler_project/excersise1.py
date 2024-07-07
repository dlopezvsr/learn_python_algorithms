
def counter(number):
    lista = []
    for i in range(1, number):
        if i % 3 == 0 or i % 5 == 0:
            lista.append(i)
    return sum(lista)

print(counter(1000))

