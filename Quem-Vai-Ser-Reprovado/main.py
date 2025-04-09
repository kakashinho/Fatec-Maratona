resp = int(input())

pessoas_e_notas = []
instancia = 0

for i in range(resp):
    entrada = input()
    nome, nota = entrada.split()
    pessoas_e_notas.append([nome, int(nota), int(instancia)])
    print(pessoas_e_notas)
    instancia += 1

ordenado = sorted(pessoas_e_notas, key=lambda x: x[1], reverse=True)

if(ordenado[resp - 2][1] == ordenado[resp - 1][1]):
    new_list = []
    new_list.append(ordenado[resp - 2][0])
    new_list.append(ordenado[resp - 1][0])

    new_list = sorted(new_list, key=lambda x: x[0], reverse=True)

    ordenado[resp - 2][0] = new_list[1]
    ordenado[resp - 1][0] = new_list[0]

print("Instancia " + str(ordenado[-1][2]))
print(ordenado[-1][0])
