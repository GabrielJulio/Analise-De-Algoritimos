def insert_sort(vetor):
    # Percorre o vetor da posicao 2 até o final
    for posicao in range(1, len(vetor)):
        posicao_anterior = posicao - 1
        while posicao_anterior >= 0 and vetor[posicao_anterior] > vetor[posicao_anterior + 1]:
            # Troca entre valor da posicao anterior com da posicao atual
            vetor[posicao_anterior], vetor[posicao_anterior + 1] = vetor[posicao_anterior + 1], vetor[posicao_anterior]
            posicao_anterior -= 1
