# Todos os passeios iniciam no estado p e terminam em q
# (p,1a), (p,1a), (p,1b) ==  aab, termina em q
# concatenando 1 1 1 = 1, custo = 1

# (p,1a), (p,1a), (p,1b), (q,2b) == aabb
# concatenando 1 1 1 2 = 2, custo = 2

# palavra "aba" custo deve ser 2
'''
2011-11-18 00:58:09 Filipe Bittencourt [UNIFEI]
considere binario a = 0 b = 1...
a = 0 = 0
b = 1 = 1
ab = 01 = 1
ba = 10 = 2
aaaa = 0000 = 0
bbbb = 1111 = 15
aabb = 0011 = 3
abbb = 0111 = 7
'''

palavra_k = ''
def main(word):
    palavra = str(word) #poderia ser o input, mas só para testar
    for x in palavra:
        if x[0] == x[1]:

        print('Palavra ')
    return 0

entrada = 'a b ab aaaa bbbb aabb abbb'
entrada.split()

main(entrada)