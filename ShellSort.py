def shell_sort(vetor):
    indice = 1
    while indice > 0:
        for posicao in range(indice, len(vetor)):
            chave = vetor[posicao]
            indice_segundo = posicao
            while indice_segundo >= indice and chave < vetor[indice_segundo - indice]:
                vetor[indice_segundo], indice_segundo = vetor[indice_segundo - indice], indice_segundo - indice
                vetor[indice_segundo] = chave
        indice = int(indice//2.2)
