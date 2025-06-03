"""
Algoritmo Shell Sort com exemplo lúdico

Descrição:
Você começa comparando "biscoitos" que estão bem distantes na bandeja
(por exemplo, a cada 4 espaços). Depois, vai diminuindo essa distância,
até comparar os vizinhos. Assim, os biscoitos vão se aproximando da posição
certa mais rapidamente!

Implementação didática com variáveis nomeadas de forma intuitiva.
"""

def shell_sort(biscoitos):
    """
    Ordena a lista de 'biscoitos' utilizando o algoritmo Shell Sort.

    Parâmetro:
    biscoitos (list): Lista de elementos numéricos (ou comparáveis).

    Retorno:
    list: A lista ordenada.
    """
    n = len(biscoitos)           # Tamanho da lista
    gap = n // 2                 # Inicializa o "gap" (distância entre os biscoitos)

    # Enquanto o gap for maior que zero, continuamos o processo
    while gap > 0:
        # Percorremos a lista a partir do índice 'gap'
        for i in range(gap, n):
            atual = biscoitos[i]  # O biscoito atual que queremos posicionar
            j = i

            # Comparamos e trocamos com elementos distantes 'gap'
            while j >= gap and biscoitos[j - gap] > atual:
                biscoitos[j] = biscoitos[j - gap]  # Move o biscoito maior para frente
                j -= gap

            # Posiciona o biscoito atual na posição correta
            biscoitos[j] = atual

        # Reduzimos a distância (gap) pela metade
        gap //= 2

    return biscoitos

# ------------------------------------------------------------------------------

if __name__ == "__main__":
    # Exemplo de uso do shell_sort

    bandeja = [64, 34, 25, 12, 22, 11, 90]

    print("Bandeja original de biscoitos:")
    print(bandeja)

    bandeja_ordenada = shell_sort(bandeja)

    print("Bandeja ordenada de biscoitos:")
    print(bandeja_ordenada)
