# Insertion Sort Exemplo das Cartas
 
Insertion Sort é um algoritmo de ordenação que organiza os elementos de uma lista inserindo cada item no lugar correto, como se você estivesse organizando cartas na mão. Imagine que você está jogando ás cartas. Você está com as cartas na mão e elas estão ordenadas. Você recebe uma nova carta e deve colocá-la na posição correta da sua mão de cartas, de forma a que as cartas obedeçam à ordenação. A cada nova carta adicionada à sua mão de cartas, a nova carta pode ser menor que algumas das cartas que você já tem na mão ou maior, e assim, você começa a comparar a nova carta com todas as cartas na sua mão até encontrar sua posição correta. Você insere a nova carta na posição correta, e, novamente, a sua mão é composta de cartas totalmente ordenadas. Então, você recebe outra carta e repete o mesmo procedimento. Então outra carta, e outra, e assim em diante, até não receber mais cartas.

Esta é a ideia por trás da ordenação por inserção. Percorra as posições do array, começando com o índice 1 (um). Cada nova posição é como a nova carta que você recebeu, e você precisa inseri-la no lugar correto no subarray ordenado à esquerda daquela posição.

# Exemplo de Funcionamento

[9, 3, 5, 1] Números utilizados em uma array para explicar sobre o Insert Sort

[9, 9, 5, 1]   → move 9

[3, 9, 5, 1]   → insere 3

[3, 9, 9, 1]   → move 9

[3, 5, 9, 1]   → insere 5

[3, 5, 9, 9]   → move 9

[3, 5, 5, 9]   → move 5

[3, 3, 5, 9]   → move 3

[1, 3, 5, 9]   → insere 1 

# Etapas de Funcionamento

1.Começa do segundo elemento (posição 1).

2.Compara o elemento atual com os anteriores.

3.Move os maiores elementos para a direita.

4.Insere o elemento atual na posição correta.

5.Repete o processo até o final da lista.

# Vantagens

1.Algoritmo de classificação estável;

2.Eficiente para listas pequenas, ordenadas, e listas quase classificadas;

3.Eficiente em termos de espaço, pois é um algoritmo no local;

4.O número de inversões é diretamente proporcional ao número de trocas (swaps);

5.Simples de entender;

6.Não necessita de espaço extra significatigo graças a oedenagem in-place;

7.Eficiente para pequenos números de dados.

# Desvantagens

1.Desenpenho proporcional ao longaritmo, ou seja, ele demora em grandes listas;

# Referências

https://pt.wikipedia.org/wiki/Insertion_sort; https://www.ime.usp.br/~pf/analise_de_algoritmos/aulas/insert.html; https://www.dio.me/articles/algoritmos-de-ordenacao-eficiencia-em-diferentes-estruturas-de-dados
