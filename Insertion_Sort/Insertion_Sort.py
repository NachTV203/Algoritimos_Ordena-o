"""
Algoritmo Insertion Sort com exemplo lúdico

Descrição:
Sabe quando você tá jogando baralho e precisa organizar as cartas na sua mão?
Então você pega uma carta e vai colocando ela no lugar certo olhando as
cartas que já estão na mão.
Se a carta que você pegou for menor que as que tão na mão você empurra elas
pra frente até achar o lugar certo pra colocar a carta.
É tipo isso que o Insertion Sort faz.
"""

def insertion_sort(cartas):
    # Aqui começa o algoritmo
    # Começa do segundo elemento porque o primeiro a gente já considera que tá na mão
    for indice_carta in range(1, len(cartas)):
        carta_atual = cartas[indice_carta]  # A carta que eu peguei pra posicionar
        posicao = indice_carta - 1          # Eu comparo com a carta da esquerda

        # Enquanto eu não chegar no começo e a carta da esquerda for maior
        # eu vou empurrando ela pra direita
        while posicao >= 0 and cartas[posicao] > carta_atual:
            cartas[posicao + 1] = cartas[posicao]  # Empurra a carta pra frente
            posicao -= 1  # Volta pra comparar com a carta anterior

        # Quando achar o lugar certo coloca a carta lá
        cartas[posicao + 1] = carta_atual

    return cartas


# --------------------------------

if __name__ == "__main__":
    # Aqui eu testei o algoritmo

    monte_de_cartas = [64, 34, 25, 12, 22, 11, 90]  # As cartas embaralhadas

    print("Monte original de cartas:")
    print(monte_de_cartas)  # Mostra as cartas bagunçadas

    cartas_ordenadas = insertion_sort(monte_de_cartas)  # Chama a função pra ordenar

    print("Monte de cartas ordenado:")
    print(cartas_ordenadas)  # Mostra as cartas organizadas
