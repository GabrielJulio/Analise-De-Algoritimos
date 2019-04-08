def selection_sort(vetor):
    # Posicao atual
    posicao1 = 0

    # Estrutura com 2 while's para verificar qual o menor número
    while posicao1 < len(vetor) - 1:
        # Menor número
        menor = posicao1
        # Proxima posicao
        posicao2 = posicao1 + 1
        while posicao2 < len(vetor):
            if vetor[posicao2] < vetor[menor]:
                menor = posicao2
            posicao2 += 1
        # Troca as posições se nescessario
        if menor != posicao1:
            vetor[posicao1], vetor[menor] = vetor[menor], vetor[posicao1]
        posicao1 += 1
