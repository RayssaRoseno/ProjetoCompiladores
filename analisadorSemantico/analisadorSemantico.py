def analisador_semantico(frase):
    pilha = [0]  # Pilha de estados
    entrada = frase.split() + ['$']  # Símbolos de entrada

    tabela = {
        (0, 'program'): 's1',
        (1, '<id>'): 's2',
        (2, ';'): 's3',
        (3, 'begin'): 's4',
        (4, 'end'): 'r5',
        (4, '$'): 'r5',
        (5, 'end'): 'r3',
        (5, '$'): 'r3',
        (6, '$'): 'accept'
    }

    regras = {
        1: ('programa', ['<id>', ';', '<corpo>']),
        2: ('<corpo>', ['begin', '<sentencas>', 'end']),
        3: ('<sentencas>', ['<sentencas>', '<sentenca>']),
        4: ('<sentencas>', []),
        5: ('<sentenca>', ['<id>', ';']),
        6: ('<id>', ['a']),
        7: ('<id>', ['b'])
    }

    symbol_table = set()  # Tabela de símbolos para armazenar os identificadores

    while True:
        estado_atual = pilha[-1]
        simbolo_atual = entrada[0]

        if (estado_atual, simbolo_atual) not in tabela:
            return False  # Erro de análise

        acao = tabela[(estado_atual, simbolo_atual)]

        if acao.startswith('s'):  # Ação Shift
            novo_estado = int(acao[1:])
            pilha.append(simbolo_atual)
            pilha.append(novo_estado)
            entrada = entrada[1:]
        elif acao.startswith('r'):  # Ação Reduce
            regra_numero = int(acao[1:])
            regra = regras[regra_numero]
            simbolo_regra = regra[0]
            tamanho_regra = len(regra[1])

            for _ in range(2 * tamanho_regra):
                pilha.pop()

            estado_atual = pilha[-1]
            pilha.append(simbolo_regra)
            pilha.append(int(tabela[(estado_atual, simbolo_regra)]))

            # Verificar regra semântica correspondente à redução
            if regra_numero == 1:  # Regra: <programa> ::= program <id>; <corpo>
                id_token = pilha[-3]  # Símbolo na posição do <id> na pilha
                if id_token not in symbol_table:
                    symbol_table.add(id_token)  # Adicionar identificador à tabela de símbolos
                else:
                    return False  # Identificador já foi declarado anteriormente

            elif regra_numero == 5:  # Regra: <sentenca> ::= <id> ;
                id_token = pilha[-2]  # Símbolo na posição do <id> na pilha
                if id_token in symbol_table:
                    return False  # Identificador já foi declarado anteriormente
                else:
                    symbol_table.add(id_token)  # Adicionar identificador à tabela de símbolos

        elif acao == 'accept':
            return True  # Análise sintática e semântica bem-sucedida


# Exemplo de uso
frase1 = 'program a ; begin a ; end'
frase2 = 'program b ;'

print(analisador_semantico(frase1))  # True
print(analisador_semantico(frase2))  # False
