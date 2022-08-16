# redes-i-dijkstra
Implementação do algoritmo de Dijkstra.
Atividade 5 da disciplina de Redes de Computadores I, ministrada na FCT-UNESP.

Para usar, basta executar o script em `dijkstra.py`.

Ele funciona a partir da leitura de um arquivo `.txt`, onde devem estar as adjacências do grafo.
Cada linha do arquivo deve conter, em ordem: vértice de origem (`char` ou `string`), vértice de destino (`char` ou `string`), peso da adjacência (aresta, `int`); separados por um espaço.
Um exemplo (`.txt` e imagem do grafo) desta estrutura de arquivo pode ser encontrado em `/exemplo`.

Para executar o exemplo (recomendável para entender o funcionamento do programa), faça:
```
> python dijkstra.py
Nome do arquivo (absoluto ou relativo): exemplo/exemplo.txt
Escolha um vértice fonte: A
```
(pode ser `A`, ou qualquer outro vértice do grafo: `B`, `C`, `D`, `E` ou `F`).

A escolha de um arquivo inválido (que não siga o padrão acima descrito) ou inexistente, ou de um vértice inválido, resultará em um erro
da linguagem Python ou em um resultado inválido (o programa não faz tratamento de erros por si).

Esta implementação, incluindo os nomes de variáveis e métodos, é baseada
nos pseudocódigos apresentados em _Introduction to Algorithms, 3rd Edition_, Cormen et al., com exceção da função `extract_min`, elaborada
por mim mesmo, baseada nas explicações do livro.