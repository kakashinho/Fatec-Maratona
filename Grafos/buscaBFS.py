from collections import deque

grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def bfs_niveis(grafo, inicio):
    visitados = set()
    fila = [inicio]
    nivel = {inicio: 0}  

    while fila:
        no = fila[0]
        fila = fila[1:]

        if no not in visitados:
            print(f"Visitando nó {no}")
            visitados.add(no)

            for vizinho in grafo.get(no, []):
                if vizinho not in visitados and vizinho not in fila:
                    fila.append(vizinho)
                    nivel[vizinho] = nivel[no] + 1 


    for no, n in nivel.items():
        print(f"Nível de {no}: {n}")

bfs_niveis(grafo, "A")
