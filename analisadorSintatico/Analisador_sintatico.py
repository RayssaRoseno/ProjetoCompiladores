# Tabela shift-reduce simplificada/ Construida com base na Tabela inicial shift-reduce que teve base na BNF principal do projeto
tabela = {
    (0, 'programa'): 's1',  # Se o estado atual é 0 e o símbolo de entrada é 'programa', realiza um "shift" para o estado 1
    (1, '<id>'): 's2',  # Se o estado atual é 1 e o símbolo de entrada é '<id>', realiza um "shift" para o estado 2
    (2, ';'): 's3',  # Se o estado atual é 2 e o símbolo de entrada é ';', realiza um "shift" para o estado 3
    (3, 'begin'): 's4',  # Se o estado atual é 3 e o símbolo de entrada é 'begin', realiza um "shift" para o estado 4
    (4, 'end'): 'r5',  # Se o estado atual é 4 e o símbolo de entrada é 'end', realiza uma "reduce" utilizando a regra 5
    (4, '$'): 'r5',  # Se o estado atual é 4 e o símbolo de entrada é '$', realiza uma "reduce" utilizando a regra 5
    (5, 'end'): 'r3',  # Se o estado atual é 5 e o símbolo de entrada é 'end', realiza uma "reduce" utilizando a regra 3
    (5, '$'): 'r3',  # Se o estado atual é 5 e o símbolo de entrada é '$', realiza uma "reduce" utilizando a regra 3
    (6, '$'): 'accept'  # Se o estado atual é 6 e o símbolo de entrada é '$', aceita a análise sintática
}

regras = {
    1: ('programa', ['<id>', ';', '<corpo>']),  # Regra 1: programa -> <id> ; <corpo>
    2: ('<corpo>', ['begin', '<sentencas>', 'end']),  # Regra 2: <corpo> -> begin <sentencas> end
    3: ('<sentencas>', ['<sentencas>', '<sentenca>']),  # Regra 3: <sentencas> -> <sentencas> <sentenca>
    4: ('<sentencas>', []),  # Regra 4: <sentencas> -> epsilon (não possui símbolos)
    5: ('<sentenca>', ['<id>', ';']),  # Regra 5: <sentenca> -> <id> ;
    6: ('<id>', ['a']),  # Regra 6: <id> -> a
    7: ('<id>', ['b'])  # Regra 7: <id> -> b
}

def analisador_sintatico(frase):
    pilha = [0]  # Pilha de estados
    entrada = frase.split() + ['$']  # Símbolos de entrada

    while True:
        estado_atual = pilha[-1]  # Obtém o estado atual
        simbolo_atual = entrada[0]  # Obtém o próximo símbolo de entrada

        if (estado_atual, simbolo_atual) not in tabela:
            return False  # Erro de análise: ação não definida na tabela

        acao = tabela[(estado_atual, simbolo_atual)]  # Obtém a ação da tabela

        if acao.startswith('s'):  # Se a ação for um "shift"
            novo_estado = int(acao[1:])  # Obtém o novo estado
            pilha.append(simbolo_atual)  # Empilha o símbolo atual
            pilha.append(novo_estado)  # Empilha o novo estado
            entrada = entrada[1:]  # Avança para o próximo símbolo de entrada
        elif acao.startswith('r'):  # Se a ação for uma "reduce"
            regra_numero = int(acao[1:])  # Obtém o número da regra
            regra = regras[regra_numero]  # Obtém a regra correspondente ao número
            simbolo_regra = regra[0]  # Obtém o símbolo não terminal da regra
            tamanho_regra = len(regra[1])  # Obtém o tamanho da regra (número de símbolos)

            for _ in range(2 * tamanho_regra):  # Desempilha 2 * tamanho_regra símbolos da pilha
                pilha.pop()

            estado_atual = pilha[-1]  # Obtém o estado atual
            pilha.append(simbolo_regra)  # Empilha o símbolo da regra
            pilha.append(int(tabela[(estado_atual, simbolo_regra)]))  # Empilha o novo estado após a redução

        elif acao == 'accept':  # Se a ação for "accept"
            return True  # Análise sintática bem-sucedida

# Exemplo de uso
frase1 = 'programa a ; begin a ; end'
frase2 = 'programa b ;'

print(analisador_sintatico(frase1))  # True
print(analisador_sintatico(frase2))  # False
