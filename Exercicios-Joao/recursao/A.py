# 1) soma dos inteiros
def soma(n):
    if n <= 1: return n #condição de parada
    return n + soma(n-1) #chamando a função para todos valores

print('A soma dos inteiros 1 a 3 =',soma(3))
print('A soma dos inteiros 1 a 10 =',soma(10))

#2) contagem dos digitos
def contagem(n):
    if n < 10: return 1
    return 1 + contagem(n//10) 

print('A contagem dos digitos 9 =', contagem(9))
print('A contagem dos digitos de 250 =', contagem(250))

#3) fatorial de um numero
def fatorial(n):
    if n <= 0: return 1 
    return n * fatorial(n-1) 

print('O fatorial de 3 =', fatorial(3))
print('O fatorial de 5 =', fatorial(5))

#4) máximo divisor comum
def mdc(n1,n2):
    if n1 % n2 == 0: return n2
    return mdc(n2, n1 % n2)

print('O máximo divisor comum de 2 e 6 é',mdc(2,6))
print('O máximo divisor comum de 11 e 13 é',mdc(11,13))

#5) Invertendo a frase
def inverter(string):
    if string: return inverter(string[1:]) + string[0] 
    return ''

print('Essa frase invertida seria:',inverter('Essa frase invertida seria:'))

#6) potenciação
def pot(n1,e1):
    if e1 <= 0: return 1
    return n1 * pot(n1, e1-1)

print('5^3 =',pot(5,3))
print('2^8 =',pot(2,8))

#7) Rotina recursiva para o problema da Torre de Hanói.
def torre_de_hanoi(n, origem, auxiliar, destino, torres):
    if n == 1:
        disco = torres[origem].pop()
        torres[destino].append(disco)
        #print(f'Move disco {disco} da torre {origem} para a torre {destino}')
    else:
        torre_de_hanoi(n-1, origem, destino, auxiliar, torres)
        disco = torres[origem].pop()
        torres[destino].append(disco)
        #print(f'Move disco {disco} da torre {origem} para a torre {destino}')
        torre_de_hanoi(n-1, auxiliar, origem, destino, torres)

def imprime_torres(torres, n):
    for nivel in range(n-1, -1, -1):
        for torre in torres:
            if len(torres[torre]) > nivel:
                print(torres[torre][nivel], end='  ')
            else:
                print(' ', end='  ')
        print()
    print('  '.join(torres) + '\n')

discos = 5
print(f'A torre de hanoi com {discos} discos')
torres = { 'A': list(range(discos, 0, -1)), 'B': [], 'C': []}

print('\nEstado inicial das torres: \n')
imprime_torres(torres, discos)

torre_de_hanoi(discos, 'A', 'B', 'C', torres)

print('\n\nEstado final das torres: \n')
imprime_torres(torres, discos)