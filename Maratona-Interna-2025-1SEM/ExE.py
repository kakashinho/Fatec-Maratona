#-------------------- TESTE ----------------------------
#def bolsa_binaria(comp,bolsas,qtd1,lucro1,qtd2,lucro2,qtd3,lucro3):

comp,bolsas = input().split()
qtd1,lucro1 = input().split()
qtd2,lucro2 = input().split()
qtd3,lucro3 = input().split()

comp    = int(comp)
bolsas  = int(bolsas)
qtd1    = int(qtd1)
qtd2    = int(qtd2)
qtd3    = int(qtd3)
lucro1  = int(lucro1) 
lucro2  = int(lucro2)
lucro3  = int(lucro3)

# 10/4 = 2 * 10 = 20
# 10/3 = 3 * 7 = 21
# 10/2 = 5 * 1 = 5

# 10/5 = 2 * 1 = 2
# 10/7 = 1 * 10 = 10
# 10/9 = 1 * 100 = 100

valor1 = int(comp/qtd1)*lucro1
valor2 = int(comp/qtd2)*lucro2
valor3 = int(comp/qtd3)*lucro3

dicionario = {f'{qtd1}': valor1, f'{qtd2}': valor2, f'{qtd3}': valor3}

ord_decrs = dict(sorted(dicionario.items(), key=lambda item: item[1], reverse=True))
primeiro = 0
segundo = 0
terceiro = 0

for n in ord_decrs:
    num = int(n)
    if int(comp/num) >= bolsas:
        if primeiro == 0: primeiro = num
        elif segundo == 0: segundo = num
        elif terceiro == 0: terceiro = num
    

resul = comp
lista = []

while (resul - primeiro) >= 0 and primeiro != 0:
    resul = resul - primeiro
    lista.append(primeiro)

    if resul-primeiro ==  segundo and segundo != 0:
        resul = resul - segundo
        lista.append(segundo)

    elif resul-primeiro ==  terceiro and terceiro != 0:
        resul = resul - terceiro
        lista.append(terceiro)


saida = 0
if not lista:
    print('IMPOSSIVEL')
else:
    for a in lista:
        if a == qtd1: saida = saida + lucro1
        elif a == qtd2: saida = saida + lucro2
        elif a == qtd3: saida = saida + lucro3
    print(saida)

#-------------------- TESTE ----------------------------
#bolsa_binaria('10','2','5','1','7','10','9','100')
#bolsa_binaria('10','3','4','4','5','5','6','6')
#bolsa_binaria('10','0','4','10','3','7','2','1')