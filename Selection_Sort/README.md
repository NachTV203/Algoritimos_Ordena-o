# 🛠️🧼📊 Selection Sort #


Selecionando o menor.
Este algoritmo é elementar. Basta percorrer o array comparando os elementos para determinar qual é o menor. No início, assumimos que o menor elemento está no índice 0 (indice_menor = 0) e iteramos a partir do segundo índice comparando os elementos.



## Exemplo:

...
	// encontra o índice do menor elemento
	int indice_menor = 0;
	for (int i = 1; i < v.length; i++) {
		if (v[i] < v[indice_menor])
			indice_menor = i;
	}

	


Ao fim da execução deste algoritmo temos uma certeza: o menor elemento está no índice 0 do array.

Como usar esta rotina para ordenar um array?
Ora, basta repetir esse mesmo processo para o restante do array. Vamos ver a execução para o values=[70,90,1,3,0,100,2]

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
 ...
public static void selectionSort(int[] v) {	--Ordenar o vetor usando selection sort
	for (int i = 0; i < v.length; i++) {  --percorre a posição do vetor
		
		int i_menor = i;   --o menor vetor está na posição  
		for (int j = i + 1; j < v.length; j++)   --percorre o restante do vetor  
			if (v[j] < v[i_menor])     --se encontrar um valor menor
				i_menor = j;    --atualiza o indice de menor valor
		
		int aux = v[i];    --guarda o valor atual
		v[i] = v[i_menor];   --coloca o menor valor na posição atual
		v[i_menor] = aux;   --Coloca o valor antigo (de i) na posição onde estava o menor
	
	}		
}
...



# Resumo #

O Selection Sort segue uma rotina bem simples e direta: encontrar o menor elemento e colocá-lo na primeira posição. A ordenação nada mais é do que aplicar essa rotina repetidas vezes para o restante do array.

# Referências #

https://joaoarthurbm.github.io/eda/posts/selection-sort/
 
