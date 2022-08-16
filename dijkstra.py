"""     
    Redes de Computadores I
    Atividade 4 - Implementação de algoritmo
    Aluno: Daniel Henrique Serezane Pereira

    A implementação aqui apresentada tenta ser o mais fidedigna possível aos
    pseudoalgoritmos do livro "Introduction to Algorithms, 3rd Edition" de
    Cormen et al., mantendo até os mesmos nomes de variáveis.

    A representação utilizada para os grafos é a de lista de adjacências. Ela está
    aliada a um dict Python, para facilitar a escrita dos algoritmos.

    Esta implementação foi baseada no meu trabalho final da disciplina de Estruturas de Dados II
    (https://github.com/Salies/edii-tpfinal).
"""

from dataclasses import dataclass
from math import inf
from copy import deepcopy

# Cada vértice é composto por: 
# - suas adjacências (e peso da adjacência)
# - predecessor no menor caminho
# - distância da fonte até o vértice (caminho mínimo)

# Esses dados não são úteis para a construção do grafo em si, com exceção
# das adjacências, afinal competem apenas ao caminho mínimo, variando conforme
# o vértice fonte. Contudo, como o único objetivo deste programa é a implementação
# do algoritmo de Dijkstra, optou-se por essa representação interna.

# Funções e estruturas
@dataclass
class vertex:
    adj: list # adjacências
    pi: str # predecessor no menor caminho
    d: int # distância da fonte até o vértice

# Inicializa os caminhos mínimos a partir da origem s.
# Atribui valores de forma que o algoritmo de Dijkstra funcione.
def initialize_single_source(G, s) -> None:
    for v in G.values():
        v.d = inf
        v.pi = None
    s.d = 0

# Faz o relaxamento da aresta u->v, de peso w.
def relax(u, uid, v, w) -> None:
    if v.d > u.d + w:
        v.d = u.d + w
        v.pi = uid

# Extrai do grafo-fila Q o vértice com menor distância até a fonte.
def extract_min(Q) -> str:
    min_k = next(iter(Q))
    min_d = Q[min_k].d
    for k, v in Q.items():
        if(v.d < min_d):
            min_k = k
            min_d = v.d
    del Q[min_k]
    return min_k

# Algoritmo de Dijkstra, baseado nos métodos anteriormente apresentados.
def dijkstra(G, s) -> None:
    initialize_single_source(G, s)
    Q = deepcopy(G)
    while Q:
        u = extract_min(Q)
        for (v, w) in G[u].adj:
            relax(G[u], u, G[v], w)

# Principal
G = {}

# Pede ao usuário o nome do arquivo, lê o arquivo de acordo com a estrutura estabelecida
# (leia README.md para mais informações) e insere os dados na representação de grafo.
filename = input("Nome do arquivo (absoluto ou relativo): ")
with open(filename) as file:
    while (line := file.readline().rstrip()):
        u, v, w = line.split(' ')
        if u not in G:
            G[u] = vertex([], None, None)
        G[u].adj.append((v, int(w)))

# A partir de um vértice fonte...
s = input('Escolha um vértice fonte: ')

# ...o algoritmo de Dijkstra é executado
dijkstra(G, G[s])

# Imprimindo os caminhos mínoimos do vértice fonte até todos os outros vértices do grafo,
# se esses caminhos exisitirem.
print(f"\nCaminhos mínimos de {s} até todos os outros vértices do grafo:")
for k, v in G.items():
    path = f"{k} " # guarda o caminho aqui
    og_d = v.d
    while(v.pi != None):
        path = f"{v.pi} -> " + path
        v = G[v.pi]
    path = f"{k}: " + path + f"(peso {('inf' if og_d == inf else og_d)})"
    print(path)