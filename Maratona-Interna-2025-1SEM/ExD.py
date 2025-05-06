num = int(input())
resul = num

 # Lista para armazenar os fatores primos e suas quantidades
div = []

# Começa tentando dividir por 2, depois 3, 4, ..., até o número e não (o -1 do numero)
for x in range(2,num+1):
    cont = 0 # Conta quantas vezes o número é divisível pelo divisor

    # Enquanto ainda for divisível, divide e conta
    while resul % x ==0:
        resul = resul / x         
        cont += 1
    # Se conseguiu dividir pelo menos uma vez, guarda o divisor e a quantidade de vezes que é fator
    if cont != 0:
        div.append(x)
        div.append(cont)

saida = ''
# For que pula de dois em dois e vai arrumando a saída para 3(2)11(1)
for x in range(0,len(div),2):
    saida = f'{saida}{div[x]}({div[x+1]})'

print(saida)
