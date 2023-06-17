tabela = {
    (0, 'programa'): 's1',
    (1, '<id>'): 's2',
    (2, ';'): 's3',
    (3, 'begin'): 's4',
    (4, 'end'): 'r5',
    (4, '$'): 'r5',
    (5, 'end'): 'r3',
    (5, '$'): 'r3',
    (6, '$'): 'accept'
}

# Gramática corrigida
regras = {
    1: ('programa', ['<id>', ';', '<corpo>']),
    2: ('<corpo>', ['begin', '<sentencas>', 'end']),
    3: ('<sentencas>', ['<sentencas>', '<sentenca>']),
    4: ('<sentencas>', []),
    5: ('<sentenca>', ['<id>', ';']),
    6: ('<id>', ['a']),
    7: ('<id>', ['b'])
}


# Função de análise sintática
def analisador_sintatico(frase):
    pilha = [0]  # Pilha de estados
    entrada = frase.split() + ['$']  # Símbolos de entrada

    while True:
        estado_atual = pilha[-1]
        simbolo_atual = entrada[0]

        if (estado_atual, simbolo_atual) not in tabela:
            return False  # Erro de análise

        acao = tabela[(estado_atual, simbolo_atual)]

        if acao.startswith('s'):
            novo_estado = int(acao[1:])
            pilha.append(simbolo_atual)
            pilha.append(novo_estado)
            entrada = entrada[1:]
        elif acao.startswith('r'):
            regra_numero = int(acao[1:])
            regra = regras[regra_numero]
            simbolo_regra = regra[0]
            tamanho_regra = len(regra[1])

            for _ in range(2 * tamanho_regra):
                pilha.pop()

            estado_atual = pilha[-1]
            pilha.append(simbolo_regra)
            pilha.append(int(tabela[(estado_atual, simbolo_regra)]))

        elif acao == 'accept':
            return True  # Análise sintática bem-sucedida

# Exemplo de uso
frase1 = 'programa a ; begin a ; end'
frase2 = 'programa b ;'

print(analisador_sintatico(frase1))  # True
print(analisador_sintatico(frase2))  # False