import ply.lex as lex

# Lista de tokens
tokens = [
    'PALAVRA_RESERVADA',
    'OPERADOR_RELACIONAL',
    'OPERADOR_ARITMETICO',
    'DELIMITADOR',
    'IDENTIFICADOR',
    'NUMERO_INTEIRO',
    'NUMERO_REAL',
    'COMENTARIO',
    'STRING',
    'CARACTER_ESPECIAL',
    'ESPACO_EM_BRANCO',
    'ERRO_LEXICO'
]

# Regras de expressões regulares para os tokens
def t_PALAVRA_RESERVADA(t):
    r'(program|var|begin|end|procedure|function|integer|real|read|write|for|to|do|repeat|until|while|if|then|else|pos)\b'
    return t

def t_OPERADOR_RELACIONAL(t):
    r'>=|<=|<>|>|<|=|\('
    return t

def t_OPERADOR_ARITMETICO(t):
    r'(\+|-|\*|/|//)'
    return t

def t_DELIMITADOR(t):
    r'[,();{}]'
    return t

def t_IDENTIFICADOR(t):
    r'[\w_]+'
    if t.value.lower() in ['program', 'var', 'begin', 'end', 'procedure', 'function', 'integer', 'real', 'read', 'write', 'for', 'to', 'do', 'repeat', 'until', 'while', 'if', 'then', 'else', 'pos']:
        t.type = 'PALAVRA_RESERVADA'
    return t

def t_NUMERO_INTEIRO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_NUMERO_REAL(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_COMENTARIO(t):
    r'(/\*(.|\n)*?\*/|//.*)'
    pass

def t_STRING(t):
    r'\"([^\\\n]|(\\.))*?\"'
    return t

def t_CARACTER_ESPECIAL(t):
    r'\'|\\\'|\\"'
    return t

def t_ESPACO_EM_BRANCO(t):
    r'\s'
    pass

def t_ERRO_LEXICO(t):
    r'[^a-zA-Z0-9_\s]'
    print(f"Erro léxico: {t.value}")
    t.lexer.skip(1)

def t_DOIS_PONTOS(t):
    r':'
    return t

# Ignorar espaços em branco e tabulações
t_ignore = ' \t'

# Função para lidar com quebra de linhas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Função para tratar erros de caracteres inválidos
def t_error(t):
    print(f"Caractere inválido: {t.value[0]}")
    t.lexer.skip(1)

# Criação do analisador léxico
lexer = lex.lex()

# Função para realizar a análise léxica do arquivo
def analyze_lexical(data):
    lexer.input(data)
    tokens = []
    while True:
        token = lexer.token()
        if not token:
            break
        tokens.append(token)
    return tokens

# Tabela de parsing LR(0) para o analisador sintático
tabela = {
    0: {'program': 's1'},
    1: {'$': 'aceita'},
    2: {'var': 's2'},
    3: {'begin': 's3'},
    4: {'end': 's4'},
    5: {'ID': 's5'},
    6: {';': 's6'},
    7: {'INTEGER': 's7'},
    8: {'REAL': 's8'},
    9: {'read': 's9'},
    10: {'write': 's10'},
    11: {'(': 's11'},
    12: {')': 's12'},
    13: {'+': 's13'},
    14: {'-': 's14'},
    15: {'*': 's15'},
    16: {'/': 's16'},
    17: {'//': 's17'},
    18: {'do': 's18'},
    19: {';': 's19'},
    20: {'to': 's20'},
    21: {'IF': 's21'},
    22: {'THEN': 's22'},
    23: {'ELSE': 's23'},
    24: {'REPEAT': 's24'},
    25: {'UNTIL': 's25'},
    26: {'WHILE': 's26'},
    27: {'<=': 's27'},
    28: {'<>': 's28'},
    29: {'<': 's29'},
    30: {'>=': 's30'},
    31: {'>': 's31'},
    32: {'=': 's32'},
    33: {'pos': 's33'},
    34: {'$': 'r1'},
    35: {'ID': 'r3'},
    36: {';': 'r3'},
    37: {'end': 'r3'},
    38: {'INTEGER': 'r3'},
    39: {'REAL': 'r3'},
    40: {'read': 'r3'},
    41: {'write': 'r3'},
    42: {'(': 'r3'},
    43: {'do': 'r3'},
    44: {';': 'r3'},
    45: {'to': 'r3'},
    46: {'IF': 'r3'},
    47: {'THEN': 'r3'},
    48: {'ELSE': 'r3'},
    49: {'REPEAT': 'r3'},
    50: {'UNTIL': 'r3'},
    51: {'WHILE': 'r3'},
    52: {'<=': 'r3'},
    53: {'<>': 'r3'},
    54: {'<': 'r3'},
    55: {'>=': 'r3'},
    56: {'>': 'r3'},
    57: {'=': 'r3'},
    58: {'pos': 'r3'},
}

# Função para realizar a análise sintática
def analisador_sintatico(tokens, tabela):
    pilha = [0]  # Pilha de estados
    indice = 0  # Índice para percorrer a lista de tokens

    while True:
        estado_atual = pilha[-1]  # Estado atual
        proximo_token = tokens[indice].type if indice < len(tokens) else '$'  # Próximo token

        # Verifica se há uma ação definida para o estado atual e o próximo token
        if proximo_token in tabela[estado_atual]:
            acao = tabela[estado_atual][proximo_token]

            if acao.startswith('s'):
                pilha.append(proximo_token)  # Empilha o próximo token
                pilha.append(int(acao[1:]))  # Empilha o próximo estado

                indice += 1  # Avança para o próximo token
            elif acao.startswith('r'):
                # Obtem a regra de redução
                regra = int(acao[1:])

                # Obtem o número de símbolos da regra de redução
                num_simbolos = len(regras_reducao[regra][1])

                # Desempilha os estados e tokens correspondentes à regra de redução
                for _ in range(num_simbolos * 2):
                    pilha.pop()

                # Estado anterior
                estado_anterior = pilha[-1]

                # Empilha o símbolo não-terminal resultante da redução
                pilha.append(regras_reducao[regra][0])

                # Empilha o próximo estado
                pilha.append(tabela[estado_anterior][regras_reducao[regra][0]])

                print(f"Redução: {regras_reducao[regra][0]} -> {regras_reducao[regra][1]}")

            elif acao == 'aceita':
                return True  # Análise sintática correta
        else:
            print("Erro de análise sintática.")
            print(f"Token encontrado: {proximo_token}")
            print(f"Token esperado: {tabela[estado_atual]}")
            return False  # Análise sintática incorreta

# Regras de redução
regras_reducao = {
    1: ('P', ['program', 'ID', '(', ')', ';', 'B']),
    2: ('B', ['var', 'D', 'S']),
    3: ('D', ['ID', ':', 'TIPO', ';', 'D']),
    4: ('D', []),
    5: ('TIPO', ['INTEGER']),
    6: ('TIPO', ['REAL']),
    7: ('S', ['begin', 'C', 'end', '.']),
    8: ('C', ['I', ';', 'C']),
    9: ('C', []),
    10: ('I', ['ID', ':=', 'EXP']),
    11: ('I', ['WHILE', 'EXP', 'DO', 'C']),
    12: ('I', ['REPEAT', 'C', 'UNTIL', 'EXP']),
    13: ('I', ['IF', 'EXP', 'THEN', 'C']),
    14: ('I', ['IF', 'EXP', 'THEN', 'C', 'ELSE', 'C']),
    15: ('I', ['read', '(', 'ID', ')']),
    16: ('I', ['write', '(', 'EXP', ')']),
    17: ('EXP', ['TERM', 'OP_REL', 'TERM']),
    18: ('TERM', ['FACTOR', 'OP_ARITM', 'TERM']),
    19: ('TERM', ['FACTOR']),
    20: ('FACTOR', ['ID']),
    21: ('FACTOR', ['NUMERO']),
    22: ('FACTOR', ['(', 'EXP', ')']),
    23: ('OP_REL', ['<=']),
    24: ('OP_REL', ['<>']),
    25: ('OP_REL', ['<']),
    26: ('OP_REL', ['>=']),
    27: ('OP_REL', ['>']),
    28: ('OP_REL', ['=']),
    29: ('OP_ARITM', ['+']),
    30: ('OP_ARITM', ['-']),
    31: ('OP_ARITM', ['*']),
    32: ('OP_ARITM', ['/']),
    33: ('OP_ARITM', ['//']),
}

# Função principal para análise léxica e sintática
def analyze_program():
    file_name = input("Digite o nome do arquivo de texto: ")

    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            file_content = file.read()

            tokens = analyze_lexical(file_content)
            if tokens:
                print("Tokens encontrados:")
                for token in tokens:
                    print(f"Tipo: {token.type}\tValor: {token.value}")

                if analisador_sintatico(tokens, tabela):
                    print("Análise sintática correta.")
                else:
                    print("Análise sintática incorreta.")
    except FileNotFoundError:
        print("Arquivo não encontrado.")

# Chama a função principal
analyze_program()
