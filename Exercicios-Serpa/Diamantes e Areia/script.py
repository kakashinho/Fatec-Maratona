numEntradas = int(input())
minasArray = []

for _ in range(numEntradas):
    valor = input()
    minasArray.append(valor)

for mina in minasArray:
    diamantes = 0
    filaAbertura = 0

    for char in mina:
        if char == "<":
            filaAbertura += 1
        elif char == ">" and filaAbertura > 0:
            filaAbertura -= 1
            diamantes += 1

    print(diamantes)




