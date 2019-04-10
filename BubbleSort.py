def bubble_sort(vetor):
    final = len(vetor)

    while final > 0:
        posicao = 0

        while posicao < final - 1:
            if vetor[posicao] > vetor[posicao + 1]:
                vetor[posicao], vetor[posicao + 1] = vetor[posicao + 1], vetor[posicao]
            posicao += 1
        final -= 1
