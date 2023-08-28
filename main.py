# Definição do grafo simplificado da Romênia
grafo = {
    "Arad": {"Sibiu": 140, "Timisoara": 118, "Zerind": 75},
    "Zerind": {"Arad": 75, "Oradea": 71},
    "Oradea": {"Zerind": 71, "Sibiu": 151},
    "Sibiu": {"Arad": 140, "Oradea": 151, "Fagaras": 99, "Rimnicu Vilcea": 80},
    "Timisoara": {"Arad": 118, "Lugoj": 111},
    "Lugoj": {"Timisoara": 111, "Mehadia": 70},
    "Mehadia": {"Lugoj": 70, "Drobeta": 75},
    "Drobeta": {"Mehadia": 75, "Craiova": 120},
    "Craiova": {"Drobeta": 120, "Rimnicu Vilcea": 146, "Pitesti": 138},
    "Rimnicu Vilcea": {"Sibiu": 80, "Craiova": 146, "Pitesti": 97},
    "Fagaras": {"Sibiu": 99, "Bucareste": 211},
    "Pitesti": {"Rimnicu Vilcea": 97, "Craiova": 138, "Bucareste": 101},
    "Bucareste": {"Fagaras": 211, "Pitesti": 101}
}

# Heurística (distância em linha reta até Bucareste)
heuristica = {
    "Arad": 366,
    "Zerind": 374,
    "Oradea": 380,
    "Sibiu": 253,
    "Timisoara": 329,
    "Lugoj": 244,
    "Mehadia": 241,
    "Drobeta": 242,
    "Craiova": 160,
    "Rimnicu Vilcea": 193,
    "Fagaras": 176,
    "Pitesti": 100,
    "Bucareste": 0
}

def busca_gulosa(grafo, heuristica, inicio, objetivo):
    visitados = set()
    caminho = []
    atual = inicio

    while atual != objetivo:
        visitados.add(atual)
        caminho.append(atual)
        vizinhos = grafo[atual]
        menor_heuristica = float("inf")
        proximo = None

        for vizinho, custo in vizinhos.items():
            if vizinho not in visitados and heuristica[vizinho] < menor_heuristica:
                menor_heuristica = heuristica[vizinho]
                proximo = vizinho

        if proximo is None:
            return None
        else:
            atual = proximo

    caminho.append(objetivo)
    return caminho

inicio = "Arad"
objetivo = "Bucareste"

caminho = busca_gulosa(grafo, heuristica, inicio, objetivo)

if caminho:
    print("Caminho encontrado:", caminho)
else:
    print("Caminho não encontrado.")
