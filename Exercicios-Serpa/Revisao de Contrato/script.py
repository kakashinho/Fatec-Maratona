listaValores = []

while True:
    valor = input()
    numeroRetirar, numeroVerificar = valor.split()

    if numeroRetirar == "0" and numeroVerificar == "0":
        break

    numeroVerificar = numeroVerificar.replace(numeroRetirar , "")

    if numeroVerificar.count("0") == len(numeroVerificar):
        numeroVerificar = "0"

    if numeroVerificar.count(numeroRetirar) == len(numeroVerificar):
        numeroVerificar = "0"


    listaValores.append(int(numeroVerificar))

for i in listaValores:
    print(i)
