    #substituição "cacharro" == "cachorro" tamanho semelhante
    #remoção "paso" == "passo" (Confere os Vizinhos) s e o
    #adição "salshicha" == "salsicha" (Confere os Vizinhos)
    #transposição "batnete" == "batente"

    #Exemplo: "tracdaoiro" == "atracadouro"
    #Erro transposição aparece "da" ao inves de "ad"

    #Desempate: transposição, remoção, substituição e adição.

#---------------------------------TESTE ----------------------------------------
def palavra(qtd,correta,erros):
    # qtd = int(input())
    # correta = input()
    # erros = input()

    qtd = int(qtd)
    correta = correta.lower()
    erros = erros.lower()
    erros = erros.split()

    words = []
    for a in erros:
        padrao = '-'*(16-len(a))
        a = '-'+a+padrao
        words.append(a)
 
    padrao = '-'*(16-len(correta))
    correta_format = '-'+correta+padrao

    dicionario = {}
    for word in words:
        qdt_erros = 0
        transposicao = 0
        remocao = 0
        substituicao = 0
        adicao = 0

        for n in range(len(word)):
                if n == 16 or n == 0 or (correta_format[n] == '-' and word[n] == '-'):
                    pula = False

                #Desempate: transposição, remoção, substituição e adição.
                #transposição "batnete" == "batente"
                elif pula and word[n] != correta_format[n]  and (word[n] == correta_format[n+1] and word[n+1] == correta_format[n]and word[n-1] != correta_format[n-1]):
                    qdt_erros += 1
                    transposicao += 1

                #remoção "paso" == "passo" (Confere os Vizinhos) s e o
                elif pula and word[n] != correta_format[n] and (word[n] == correta_format[n+1]):
                    qdt_erros += 1
                    remocao += 1

                 #substituição "cacharro" == "cachorro" tamanho semelhante
                elif pula and word[n] != correta_format[n] and (correta_format[n+1] == word[n+1] and correta_format[n-1] == word[n-1]):
                    qdt_erros += 1
                    substituicao += 1
                #adição "salshicha" == "salsicha" (Confere os Vizinhos)
                elif pula and word[n] != correta_format[n] and (correta_format[n] == word[n+1] and correta_format[n-1] == word[n-1]):
                    qdt_erros += 1
                    adicao += 1
                pula = True
        dicionario[word] = (qdt_erros,adicao,substituicao,remocao,transposicao)

    ord_decrs = dict(sorted(dicionario.items(), key=lambda item: item[1], reverse=False))

    palavra = "".join(list(ord_decrs.keys())[0])

    saida = ''
    for ltr in palavra:
        if ltr != '-':
            saida = f'{saida}{ltr}'

    print(ord_decrs)
    
palavra(5,'Semelhante', 'similhante emelhaante semelhnat diferente samalhente')
palavra(7,'componente', 'contonenti omponent comopnenT camponete Componentes porcelana cachorros')
palavra(3, 'cachorro', 'cacharro cachurro cachorroo') #cacharro
palavra(4, 'batente', 'batnete batetne batntee bantete') #batnete
palavra(4, 'atracadouro', 'tracdaoiro atracadurro atraacadouro atracadoro') #tracdaoiro