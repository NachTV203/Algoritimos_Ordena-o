# QuickSort

QuickSort, sem duvida, se sobresai como um dos algoritmos de ordenação mais velozes e eficientes, concebido pelo cientista da computação britânico C. A. R. Hoare, la em 1960. O algoritmo, ele funciona sob a estratégia de dividir para conquistar, ou seja, seleciona um elemento chave, o pivô, e logo depois reorganiza os demais de forma que os menores fiquem à esquerda e os maiores, à direita. Essa etapa de reorganização é conhecida como particionamento. Feito isso, o pivô já está onde deveria estar, e o algoritmo então repete essa operação nas duas sublistas resultantes, aquelas que ainda não estão ordenadas.

Particionamento pelo método de Lomuto, tipo assim
Uma das maneiras mais populares de executar essa divisão é usando o método de Lomuto, que normalmente escolhe o pivô no começo ou no fim da lista. Nele, dois índices são usados: um para analisar os elementos e outro para indicar a posição dos elementos menores ou iguais ao pivô. Toda vez que encontra um número menor ou igual ao pivô, acontece uma troca de posições. Esse processo persiste até que o intervalo definido acabe.
Apesar de ser descomplicado e fácil de se compreender, o método Lomuto pode numas situações ser ineficiente, tipo quando a lista já tá ordenada ou cheia de itens iguais. Nesses casos, a complexidade do algoritmo pode subir pra O(n²). Pra não ter isso, dá pra usar outras táticas, tipo escolher o pivô de maneira mais esperta, usar outros métodos (como o Insertion Sort em listas pequenas) e jeitos mais eficientes de tratar elementos repetidos.

Casos de performance

A performance do QuickSort pode mudar bastante conforme o particionamento é feito:

• Pior caso: acontece quando o pivô divide a lista de forma beeem desigual, tipo colocando tudo num só lado. Isso gera muitas chamadas recursivas e o tempo sobe pra O(n²).
• Melhor caso: ocorre quando o pivô divide a lista quase que ao meio. Assim, o algoritmo trabalha melhor, chegando numa complexidade média de O(n log n).
Estabilidade do Algoritmo

QuickSort num é um algoritmo estável, entende? Elementos com o mesmo valor pode ser que tenham suas posições relativas trocadas durante a ordenação. Isso ocorre porque, nas trocas feitas, o algoritmo ignora a ordem original dos elementos idênticos.

Apesar d'existirem jeitos de deixar o QuickSort estável, essas mudanças pedem modificações no processo de partição, e com isso a velocidade do algoritmo pode diminuir. Por isso, normalmente, a gente escolhe a versão original quando a estabilidade num é uma necessidade grande.
