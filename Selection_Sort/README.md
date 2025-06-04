# 🛠️📊 Selection Sort #


Selecionando o menor.
O Selection Sort é um algoritmo de ordenação simples que funciona selecionando o menor elemento não ordenado e movendo-o para a posição correta. Em cada passo, o algoritmo encontra o elemento mínimo na parte não ordenada da lista e troca com o elemento na posição atual. Esse processo é repetido até que toda a lista esteja ordenada.


## Exemplo:

 Vamos ver a execução para o values=[70,90,1,3,0,100,2]

Na primeira execução, 0 é o menor valor. Encontramos esse valor e trocamos com a primeira posição (70).

[70, 90, 1, 3, 0, 100, 2]

[0, 90, 1, 3, 70, 100, 2]

Agora, aplicamos a mesma ideia para o restante do array, ou seja, no intervalo de índices [1,values.length−1].

[0, 90, 1, 3, 70, 100, 2]

[0, 1, 90, 3, 70, 100, 2]

Depois, aplicamos a mesma ideia para o restante do array, ou seja, no intervalo de índices [2,values.length−1].

[0, 1, 90, 3, 70, 100, 2]

[0, 1, 2, 3, 70, 100, 90]

Continuamos aplicando a mesma ideia para o restante do array, ou seja, no intervalo de índices [3,values.length−1]
. Como 3 já está no seu lugar, ele será trocado por ele mesmo. O mesmo acontece com o intervalo de índices [4,values.length−1], onde 70 já está em sua posição.

Aplicando, então, para o intervalo de índices [5,values.length−1], temos:

[0, 1, 2, 3, 70, 100, 90]

[0, 1, 2, 3, 70, 90, 100]

Por fim, aplicado para o intervalo [6,values.length−1], temos que 100 já está em sua posição.

Feito! O array está ordenado. Note que apenas executamos a rotina de encontrar o menor e colocar na primeira posição várias vezes. Para ser exato, executamos N
 vezes, variando a faixa de valores que o algoritmo deve avaliar.




# Resumo #

O Selection Sort segue uma rotina bem simples e direta: encontrar o menor elemento e colocá-lo na primeira posição. A ordenação nada mais é do que aplicar essa rotina repetidas vezes para o restante do array.

# 📚Referências #

https://joaoarthurbm.github.io/eda/posts/selection-sort/
 
