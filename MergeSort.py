def merge_sort(vetor, pi, pf):
    # Posicao inicial e final do vetor
    if pi < pf:
        # Posicao media do vetor (retornado apenas parte inteira)
        pm = (pi + pf) // 2
        # Merge-Sort para primeira metade do vetor
        merge_sort(vetor, pi, pm)
        # Merge-Sort para segunda metade do vetor
        merge_sort(vetor, pm + 1, pf)
        # Unindo vetores
        merge(vetor, pi, pm, pf)


def merge(vetor, pi, pm, pf):
    # Mantendo uma copia salva do vetor
    copia = vetor.copy()
    # Indicie para percorrer os vetores
    i = pi
    j = pm + 1
    k = pi
    while k <= pf:
        if i > pm:
            vetor[k] = copia[j]
            j += 1

        elif j > pf:
            vetor[k] = copia[i]
            i += 1

        elif copia[i] <= copia[j]:
            vetor[k] = copia[i]
            i += 1

        else:
            vetor[k] = copia[j]
            j += 1

        k += 1
