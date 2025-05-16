from collections import deque

def percorrer_grafo(inicio, fim, grafo):
    visitados = set()
    fila = deque([inicio])
    caminho = {inicio : None}

    while fila:
        no = fila.popleft()

        if no == fim:
            break

        if no not in visitados:
            visitados.add(no)

            for vizinho in grafo[no]:
                fila.append(vizinho)
                caminho[vizinho] = no

    if fim not in caminho:
        return "sem conexao"
    
    rota = []
    atual = fim

    while atual is not None:
        rota.append(atual)
        atual = caminho[atual]
    
    return len(rota)



conexoes = []
conexoesParaSaber = []

grafo = {}



quantidadeConexoes = int(input())

for i in range(quantidadeConexoes + 1):
    nomes = input()
    conexao = nomes.split()
    
    if conexao[0] not in grafo:
        grafo[conexao[0]] = []

    grafo[conexao[0]].append(conexao[1])

while True:
    nome = input()
    if(nome == "* *"):
        break
    conexoesParaSaber.append(nome)


for i in conexoesParaSaber:
    nomeSplit = i.split()
    caminho = percorrer_grafo(nomeSplit[0], nomeSplit[1], grafo)
    print(f"{nomeSplit[0]}-{nomeSplit[1]} = {caminho}")


