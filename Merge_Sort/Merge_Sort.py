"""
Algoritmo Merge Sort com exemplo lúdico

Descrição:
Sabe quando você tem várias pilhas de figurinhas tudo bagunçada?
Aí você fica separando elas no meio até ficar bem pequenininha, tipo uma figurinha só.
Depois você vai juntando de novo, só que sempre deixando elas em ordem.

No fim, vira uma pilha grandona, só que toda certinha.
É isso que o Merge Sort faz.
"""

def merge_sort(figurinhas):
    # Se a lista tiver só uma ou nenhuma já tá ordenada, então retorna ela
    if len(figurinhas) <= 1:
        return figurinhas

    # Aqui eu divido a lista no meio
    meio = len(figurinhas) // 2
    lado_esquerdo = merge_sort(figurinhas[:meio])  # Chama de novo pra ordenar o lado esquerdo
    lado_direito = merge_sort(figurinhas[meio:])   # E aqui chama pra ordenar o lado direito

    # Agora junta os dois lados só que em ordem certinha
    return juntar(lado_esquerdo, lado_direito)


def juntar(esquerda, direita):
    pilha_ordenada = []  # Aqui vai ficar a pilha toda organizada
    i = 0  # Controla onde eu tô na esquerda
    j = 0  # Controla onde eu tô na direita

    # Enquanto ainda tiver coisa nas duas listas eu comparo e pego a menor
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            pilha_ordenada.append(esquerda[i])  # Pego da esquerda
            i += 1  # Ando pra próxima da esquerda
        else:
            pilha_ordenada.append(direita[j])  # Pego da direita
            j += 1  # Ando pra próxima da direita

    # Se sobrou coisa na esquerda, joga tudo na pilha ordenada
    while i < len(esquerda):
        pilha_ordenada.append(esquerda[i])
        i += 1

    # Mesma coisa se sobrou na direita
    while j < len(direita):
        pilha_ordenada.append(direita[j])
        j += 1

    return pilha_ordenada


# ------------------------------------------------------------------------------

if __name__ == "__main__":
    # Testando pra ver se deu certo

    pilha_de_figurinhas = [64, 34, 25, 12, 22, 11, 90]  # As figurinhas tudo bagunçada

    print("Pilha de figurinhas antes de arrumar:")
    print(pilha_de_figurinhas)  # Mostra como tá antes

    figurinhas_ordenadas = merge_sort(pilha_de_figurinhas)  # Aqui chama pra ordenar

    print("Pilha de figurinhas depois de arrumar:")
    print(figurinhas_ordenadas)  # Mostra como ficou depois
