#8)  n-ésimo elemento da sequência de Fibonacci
def fibonacci(n):
    if n <= 2: return 1
    return fibonacci(n-1) + fibonacci(n-2)

print('O terceiro numero de fibonnaci é', fibonacci(3))
print('O quinto numero de fibonnaci é', fibonacci(5))
print('O sétimo numero de fibonnaci é', fibonacci(7))

#9)  recebe uma lista de números e retorna o maior
def maior(lista):
    print(lista)
    if not lista[1:]:  # Caso base: só tem um elemento
        return lista[0]
    
    # Chamada recursiva
    maior_lista = maior(lista[1:])

    resultado = lista[0] if lista[0] > maior_lista else maior_lista
    print(f'Comparando {lista[0]} com {maior_lista} -> {resultado}')
    
    return resultado


numeros = [4, 10, 2, 89, 3, 55]
print('O maior numero da lista [4, 10, 2, 89, 3, 55] é', maior(numeros))