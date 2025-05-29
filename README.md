# Algoritmos de Ordenação em Python Utilizando `sort`

Este repositório tem como objetivo demonstrar a implementação de algoritmos clássicos de ordenação utilizando a linguagem Python. Os algoritmos abordados são:

- Bubble Sort  
- Selection Sort  
- Insertion Sort  
- Shell Sort  
- Merge Sort  
- Quick Sort

A ordenação de dados é uma das operações fundamentais na ciência da computação, desempenhando papel crucial em diversas aplicações, desde a organização de informações até a otimização de algoritmos de busca e estruturas de dados. Cada algoritmo aqui apresentado possui características específicas quanto à sua complexidade, estabilidade e eficiência, sendo amplamente discutidos na literatura acadêmica.

As implementações seguem os conceitos descritos em fontes reconhecidas na área de algoritmos e estruturas de dados, como:

- Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022). *Introduction to Algorithms* (4th ed.). MIT Press.  
- Sedgewick, R., & Wayne, K. (2011). *Algorithms* (4th ed.). Addison-Wesley.  
- Ziviani, N. (2018). *Algoritmos: Teoria e Prática* (3ª ed.). Cengage Learning.

Este repositório é indicado para estudantes, entusiastas e profissionais que desejam entender e comparar o funcionamento interno de diferentes métodos de ordenação através de exemplos práticos em Python.

---

## 📂 Estrutura do Projeto

```
algoritmos-de-ordenacao/
├── bubble_sort.py
├── selection_sort.py
├── insertion_sort.py
├── shell_sort.py
├── merge_sort.py
├── quick_sort.py
├── main.py
└── README.md
```

Cada arquivo contém a implementação individual de um algoritmo. O arquivo `main.py` pode ser utilizado para executar e testar os algoritmos com listas de exemplo.

---

## 🚀 Como Executar

### Pré-requisitos

- Python 3.8 ou superior instalado no sistema

### Executar um algoritmo individual

```bash
python bubble_sort.py
```

Ou utilizar o `main.py` para comparar múltiplos algoritmos:

```bash
python main.py
```

---

## 📈 Exemplos de Uso

Exemplo de ordenação com Bubble Sort:

```python
from bubble_sort import bubble_sort

lista = [5, 2, 9, 1, 5, 6]
ordenada = bubble_sort(lista)
print(ordenada)
# Saída: [1, 2, 5, 5, 6, 9]
```

---

## 🧠 O que você aprenderá

- Diferenças entre algoritmos estáveis e instáveis
- Análise de complexidade de tempo (melhor, médio e pior caso)
- Aplicações práticas e eficiência de cada algoritmo

---

## 📚 Referências

- Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022). *Introduction to Algorithms* (4th ed.). MIT Press.  
- Sedgewick, R., & Wayne, K. (2011). *Algorithms* (4th ed.). Addison-Wesley.  
- Ziviani, N. (2018). *Algoritmos: Teoria e Prática* (3ª ed.). Cengage Learning.

---

## 📝 Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.

---

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.
