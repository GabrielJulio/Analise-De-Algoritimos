import time

começo = time.time()
#Abrindo o arquivo de texto com o nome especificado
numeros_em_txt = open('Numeros desordenados.txt', 'r')

#Removendo espaços e armazenando os numeros em uma Lista
numeros = numeros_em_txt.read().split()

#Fechando o arquivo original para remover objeto da memória
numeros_em_txt.close()

#Transformando Texto em Inteiro
for posicao in range(0, len(numeros)):
    numeros[posicao] = int(numeros[posicao])


#Ordenando os números em ordem crescente
for posicao in range(1, len(numeros)):
    posicao_anterior = posicao - 1
    while posicao_anterior >=0 and numeros[posicao_anterior] > numeros[posicao_anterior + 1]:
        numeros[posicao_anterior], numeros[posicao_anterior + 1] = numeros[posicao_anterior + 1], numeros[posicao_anterior]
        posicao_anterior -= 1


#Transformando Inteiro em Texto
for posicao in range(0, len(numeros)):
    numeros[posicao] = str(numeros[posicao])

#Transformando Lista em Texto separando seu conteúdo por espaço
numeros_em_texto_ordenados = ' '.join(numeros)

#Criando arquivo de texto, escrevendo os números no arquivo e salvando
novo_arquivo_txt_com_numeros_ordenados = open('Numeros ordenados.txt', 'w+')
novo_arquivo_txt_com_numeros_ordenados.write(numeros_em_texto_ordenados)
novo_arquivo_txt_com_numeros_ordenados.close()
fim = time.time() - começo

print('Processo de ordenação de todos os números foi exatamente {} segundos.'.format(fim))
