import random

quantidade_de_numeros = random.randint(1, 10000)
numeros_aleatorios = str(random.randint(1, 10000))

for numero_aleatorio in range(quantidade_de_numeros):
    numeros_aleatorios += ' ' + str(random.randint(1, 10000))

numeros_desordenados = open('Numeros desordenados.txt', 'w+')
numeros_desordenados.write(numeros_aleatorios)
numeros_desordenados.close()
