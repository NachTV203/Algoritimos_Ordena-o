"""
Algoritmo Bubble Sort com exemplo lúdico

Descrição:
Imagine que você está organizando uma fila de bolhas de sabão por tamanho
Você começa comparando bolhas vizinhas e, se a da frente for menor que a de trás
elas trocam de lugar. assim a maior bolha vai subindo até o final da fila
como se estivesse subindo na água bolha por bolha.
Você repete isso várias vezes até que todas as bolhas estejam na ordem certa
do menor para o maior (ou do maior para o menor se quiser)
Implementação didática com variáveis nomeadas de forma intuitiva.
"""

def bubble_sort(bolhas):
    """
    Ordena a lista de bolhas utilizando o algoritmo Bubble Sort
    Parâmetro:
    bolhas (list): Lista de elementos numéricos (ou comparáveis)
    Retorno:
    list: A lista ordenada
    """
    n = len(bolhas)  # Quantidade de bolhas na fila

    # Percorre todas as bolhas
    for passada in range(n):
        # A cada passada as maiores bolhas vão ficando no final
        for i in range(0, n - passada - 1):
            bolha_atual = bolhas[i]
            bolha_vizinha = bolhas[i + 1]

            # Se a bolha atual for maior que a vizinha troca de lugar
            if bolha_atual > bolha_vizinha:
                bolhas[i], bolhas[i + 1] = bolhas[i + 1], bolhas[i]
                # As bolhas se empurram para a ordem certa

    return bolhas


# ------------------------------------------------------------------------------

if __name__ == "__main__":
    # Exemplo do uso do bubble_sort

    fila_de_bolhas = [64, 34, 25, 12, 22, 11, 90]

    print("Fila original de bolhas de sabão:")
    print(fila_de_bolhas)

    fila_ordenada = bubble_sort(fila_de_bolhas)

    print("Fila ordenada de bolhas de sabão:")
    print(fila_ordenada)
