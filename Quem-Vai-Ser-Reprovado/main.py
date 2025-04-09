
r = int(input())

lista_alunos = []
nomes = []
notas = []

for i in range(r):
    entrada = input()
    nomes,notas = entrada.split()
    lista_alunos.append({
        "nome" : nomes,
        "nota": int(notas)
    })
    if(i == len(r - 1) )

alunos_ordenados = sorted(lista_alunos, key=lambda x: x["nota"])

print(alunos_ordenados)

    
    
    