"""
Algoritmo Selection Sort com exemplo lúdico

Descrição:
Pensa que você tem uma lista de figurinhas toda bagunçada.
O jeito que o Selection Sort funciona é: ele procura a menor figurinha da lista toda
e troca ela com a que está no começo.

Depois ele faz a mesma coisa pro resto da lista,
sempre pegando a menor que ainda não está no lugar certo.
No final, tudo fica organizado.
"""

def selection_sort(figurinhas):
    n = len(figurinhas)  # Quantidade total de figurinhas

    # Passa por toda a lista menos o último elemento
    for i in range(n - 1):
        posicao_menor = i  # Assume que o menor tá aqui no começo

        # Procura a menor figurinha depois da posição i
        for j in range(i + 1, n):
            if figurinhas[j] < figurinhas[posicao_menor]:
                posicao_menor = j  # Atualiza pra posição da menor que encontrou

        # Troca a figurinha da posição i com a menor que achou
        figurinhas[i], figurinhas[posicao_menor] = figurinhas[posicao_menor], figurinhas[i]

    return figurinhas


# ------------------------------------------------------------------------------

if __name__ == "__main__":
    # Testando pra ver se funciona

    pilha_de_figurinhas = [64, 34, 25, 12, 22, 11, 90]  # Lista bagunçada

    print("Antes de ordenar")
    print(pilha_de_figurinhas)  # Mostra como tá antes

    figurinhas_ordenadas = selection_sort(pilha_de_figurinhas)  # Ordena as figurinhas

    print("Depois de ordenar")
    print(figurinhas_ordenadas)  # Mostra como ficou no final
