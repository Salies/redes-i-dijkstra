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

@dataclass
class vertex:
    adj: list # adjacências
    pi: str # predecessor no menor caminho
    d: int # distância da fonte até o vértice

def initialize_single_source(G, s):
    for v in G.values():
        v.d = inf
        v.pi = None
    s.d = 0

def relax(u, uid, v, w):
    if v.d > u.d + w:
        v.d = u.d + w
        v.pi = uid

def extract_min(Q):
    min_k = next(iter(Q))
    min_d = Q[min_k].d
    for k, v in Q.items():
        if(v.d < min_d):
            min_k = k
            min_d = v.d
    del Q[min_k]
    return min_k

def dijkstra(G, s):
    initialize_single_source(G, s)
    Q = deepcopy(G)
    while Q:
        u = extract_min(Q)
        for (v, w) in G[u].adj:
            relax(G[u], u, G[v], w)

# Grafo apresentado no slide da aula
G = {
    'A': vertex([('B', 2), ('C', 5), ('D', 1)], None, None),
    'B': vertex([('A', 2), ('C', 3), ('D', 2)], None, None),
    'C': vertex([('A', 5), ('B', 3), ('D', 3), ('E', 1), ('F', 5)], None, None),
    'D': vertex([('A', 1), ('B', 2), ('C', 3), ('E', 1)], None, None),
    'E': vertex([('C', 1), ('D', 1), ('F', 2)], None, None),
    'F': vertex([('C', 5), ('E', 2)], None, None)
}

s = 'A'
dijkstra(G, G[s])

print(f"Caminhos mínimos de {s} até todos os outros vértices do grafo:")
for k, v in G.items():
    print(k, v.adj, v.d, v.pi)