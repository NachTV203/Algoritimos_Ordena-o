# 🛠️🧼📊 Algoritmo Bubble Sort: A Base da Ordenação!

O **Bubble Sort**, hum, é um algoritmo de ordenação simples, certo? 

Que age comparando repetidamente pares de elementos vizinhos, e trocando-os se não estiverem na ordem correta – tipo, pra ordem crescente, se o da esquerda for maior que o da direita.

Esse processo se repete até que nenhuma troca seja precisa numa passada completa pela lista, sinalizando que a lista, enfim, está organizada.

## Exemplo:

```
[5, 2, 8, 4, 1] Números utilizados em uma array para explicar sobre o Bubble Sort

-> [2, 5, 8, 4, 1]
-> [2, 5, 4, 8, 1]
-> [2, 5, 4, 1, 8] (8 vai para o fim)
```

## Como funciona:

1. Vai-se percorrendo a lista, começando pela esquerda.
2. A gente compara os elementos um do lado do outro.
3. Quando o da esquerda é maior que o da direita, pro jeito que cresce, troca a posição.
4. Depois da primeira vez, o maior "sobe" pro lugar certo, lá no fim.
5. Aí repete, mas só com o que sobrou, já no fim não mexe mais.
6. E dá pra parar antes, se numa passada nada mudar, quer dizer tá tudo certo!

## Pontos positivos do Bubble Sort são esses:

- Implementá-lo é simples, sendo mesmo um dos algoritmos de ordenação mais fáceis de entender e por em prática. Isso faz dele uma ótima forma de começar a estudar os algoritmos de ordenação, entende?

- O uso baixo de memória, ou espaço O(1), é outra coisa boa porque ele atua "in-place". Ele organiza os dados dentro da estrutura original, só usando uma variável pra fazer as trocas. A necessidade de mais memória é, então, bem pequena, conforme o tamanho dos dados originais.

- O Bubble Sort também mantém a ordem dos valores iguais. Depois que o algoritmo roda, a ordem dos valores iguais no arranjo de dados não muda.

- Pra listas quase prontas, com um ajuste, o algoritmo pode ser bom. Uma versão otimizada que para se nenhuma troca é feita numa rodada pode ser rápida, chegando a uma complexidade O(n), no melhor dos casos.

- Além disso, o algoritmo vê rápido se a lista já tá pronta, e para de rodar com base nessa otimização que acabamos de ver.


## Pontos Negativos do Bubble Sort:


- Trocas exageradas: Ele pode causar um monte de trocas, o que as vezes é caro, dependendo dos dados e da troca em si.

- Ineficiente, sem otimizações: O Bubble Sort normal sempre realiza a mesma quantidade de comparações, não importa a ordem da lista. Embora existam melhorias, elas não o deixam competitivo contra algoritmos mais avançados.

- O Problema das "Tartarugas": Itens pequenos no final da lista ("tartarugas") se movem devagar, só uma posição por vez a cada passagem. Mas itens grandes no começo ("coelhos") vão rápido pro fim.

- Quase nunca a Melhor Opção: Dada sua falta de eficiência, dificilmente eh a melhor opção em aplicações reais, exceto talvez em conjuntos de dados muito pequenos ou pra fins de aprendizado.

- Os algoritmos preferidos são aqueles como Merge Sort Quick Sort, ou mesmo o Insertion Sort que por ventura demonstra uma complexidade O(n²) no entanto pode ser mais ligeiro na prática.
