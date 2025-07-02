from collections import deque

numeroInputs = int(input())

grafoConexoes = {}
conexoesParaSaber = []

for i in range(numeroInputs + 1):
    if i == numeroInputs:
        input()
        break
    
    conexao = input()
    nomeNo, nomeConexao = conexao.split()

    if nomeNo not in grafoConexoes:
        grafoConexoes[nomeNo] = []

    if nomeConexao not in grafoConexoes:
        grafoConexoes[nomeConexao] = []

    grafoConexoes[nomeNo].append(nomeConexao)
    grafoConexoes[nomeConexao].append(nomeNo)

while True:
    conexao = input()
    if conexao == "* *":
        break
    nomeNo, nomeConexao = conexao.split()

    conexoesParaSaber.append([nomeNo, nomeConexao])



for i in conexoesParaSaber:
    visitados = set()
    origem = i[0]
    target = i[1]
    fila = deque([(origem, 0)])
    encotrado = False
    while fila:
        no, passos = fila.popleft()

        if no == target:
            print(origem + "-" + target + " = " + str(passos))
            encotrado = True
            break

        if no not in visitados:
            visitados.add(no)
            for vizinho in grafoConexoes.get(no, []):
                if vizinho not in fila and vizinho not in visitados:
                    fila.append((vizinho, passos + 1))
    if not encotrado:
        print(origem + "-" + target + " = sem conexao")

        


