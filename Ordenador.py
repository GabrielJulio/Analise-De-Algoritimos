from InsertSort import insert_sort
from MergeSort import merge_sort
from SelectionSort import selection_sort
from BubbleSort import bubble_sort
from ShellSort import shell_sort
from CocktailSort import cocktail_sort
import time

# Abrindo o arquivo de texto com o nome especificado
nome_do_arquivo = input('Qual o nome do arquivo (com a extensão)? ')
numeros_em_txt = open(nome_do_arquivo, 'r')

# Removendo espaços e armazenando os numeros em uma Lista
numeros = numeros_em_txt.read().split()

# Fechando o arquivo original para remover objeto da memória
numeros_em_txt.close()

# Transformando Texto em Inteiro
for posicao in range(0, len(numeros)):
    numeros[posicao] = numeros[posicao]

# alg é o algoritmo escolhido
alg = 0
while alg == 1 or 2 or 3 or 4:
    alg = int(input('Qual algoritmo você deseja utilizar?\n1 - Insert-Sort\n2 - Merge-Sort\n3 - Selection-Sort\n'
                    '4 - Bubble-Sort\n5 - Shell-Sort\n6 - Cocktail-Sort'))
    if alg == 1:
        comeco = time.time()
        insert_sort(numeros)
        fim = time.time() - comeco
        alg = 'Insert-Sort'
        break
    elif alg == 2:
        comeco = time.time()
        merge_sort(numeros, 0, len(numeros)-1)
        fim = time.time() - comeco
        alg = 'Merge-Sort'
        break
    elif alg == 3:
        comeco = time.time()
        selection_sort(numeros)
        fim = time.time() - comeco
        alg = 'Selection-Sort'
        break
    elif alg == 4:
        comeco = time.time()
        bubble_sort(numeros)
        fim = time.time() - comeco
        alg = 'Bubble-Sort'
        break
    elif alg == 5:
        comeco = time.time()
        shell_sort(numeros)
        fim = time.time() - comeco
        alg = 'Shell-Sort'
    elif alg == 6:
        comeco = time.time()
        cocktail_sort(numeros)
        fim = time.time() - comeco
        alg = 'Cocktail-Sort'
        break
    else:
        print('Você digitou uma opção incorreta, tente novamente')


# Transformando Inteiro em Texto
for posicao in range(0, len(numeros)):
    numeros[posicao] = str(numeros[posicao])

# Transformando Lista em Texto separando seu conteúdo por espaço
numeros_em_texto_ordenados = ' '.join(numeros)

# Criando arquivo de texto, escrevendo os números no arquivo e salvando
novo_arquivo_txt_com_numeros_ordenados = open('Numeros ordenados.txt', 'w+')
novo_arquivo_txt_com_numeros_ordenados.write(numeros_em_texto_ordenados)
novo_arquivo_txt_com_numeros_ordenados.close()


print('Processo de ordenação de todos os números foi exatamente {0} segundos com o algoritmo {1}.'.format(fim, alg))
print('Você pode conferir os números ordenados em um arquivo chamado "Numeros ordenados.txt"')
