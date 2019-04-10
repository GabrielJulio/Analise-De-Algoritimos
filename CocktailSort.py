import random

def cocktail_sort(vetor):
    vetor_novo = []
    for posicaoA in range(len(vetor)):
        for posicaoB in range(len(vetor) - 1):
            if vetor[len(vetor)-1 - posicaoB] < vetor[len(vetor)-2 - posicaoB]:
                vetor[len(vetor) - 1 - posicaoB], vetor[len(vetor)-2 - posicaoB] = vetor[len(vetor)-2 - posicaoB],vetor[len(vetor)-1 - posicaoB]
            if vetor[posicaoB] > vetor[posicaoB + 1]:
                vetor[posicaoB], vetor[posicaoB + 1] = vetor[posicaoB + 1], vetor[posicaoB]


vetor = list(range(0, 10))
random.shuffle(vetor)
cocktail_sort(vetor)
print(vetor)
