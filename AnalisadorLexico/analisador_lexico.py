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
    while True:
        token = lexer.token()
        if not token:
            break
        print(f"Token: {token.type}\tValor: {token.value}")

# Leitura do arquivo
file_name = input("Digite o nome do arquivo de texto: ")
try:
    with open(file_name, 'r', encoding='utf-8') as file:
        file_content = file.read()
        analyze_lexical(file_content)
except FileNotFoundError:
    print("Arquivo não encontrado.")
