"""
Algoritmo QuickSort com exemplo lúdico

Descrição:
Imagina que você está separando figurinhas
Você escolhe uma figurinha que vira o pivô
Depois separa as menores pra um lado e as maiores pro outro
Faz isso com cada lado até que tudo fique organizado
É como se fosse dividir até ficar tudo certo
"""

def quicksort(figurinhas):
    # Se a lista tiver um ou nenhum elemento já está ordenada
    if len(figurinhas) <= 1:
        return figurinhas

    # Escolhe o pivô aqui peguei o primeiro da lista
    pivo = figurinhas[0]

    # Cria duas listas
    menores = []  # Lista onde ficam as figurinhas menores ou iguais ao pivô
    maiores = []  # Lista onde ficam as figurinhas maiores que o pivô

    # Percorre as outras figurinhas comparando com o pivô
    for figurinha in figurinhas[1:]:
        if figurinha <= pivo:
            menores.append(figurinha)  # Se for menor ou igual vai pra lista dos menores
        else:
            maiores.append(figurinha)  # Se for maior vai pra lista dos maiores

    # Agora faz o quicksort nos menores e nos maiores e junta tudo
    return quicksort(menores) + [pivo] + quicksort(maiores)


# ------------------------------------------------------------------------------

if __name__ == "__main__":
    # Teste do algoritmo

    pilha_de_figurinhas = [64, 34, 25, 12, 22, 11, 90]  # Lista das figurinhas desorganizadas

    print("Pilha de figurinhas antes de ordenar")
    print(pilha_de_figurinhas)  # Mostra a lista antes

    figurinhas_ordenadas = quicksort(pilha_de_figurinhas)  # Chama o quicksort pra ordenar

    print("Pilha de figurinhas depois de ordenar")
    print(figurinhas_ordenadas)  # Mostra como ficou depois
