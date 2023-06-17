## Lexico 

Lexico - Compilador simples desenvolvido em Python que realiza a análise léxica de um arquivo de texto seguindo uma determinada gramática(BNF).

## Funcionalidades Lexica

- Análise léxica de arquivos de texto;
- Identificação e classificação de tokens, como palavras reservadas, operadores, delimitadores, identificadores, números e outros;
- Tratamento de erros léxicos.

## Requisitos

- Python 3.x

## Como usar

    
  1. Clone este repositório:
    
``git clone https://github.com/RayssaRoseno/ProjetoCompiladores/tree/main``


  2. Navegue até o diretório do projeto:

``cd compilador``


  3. Execute o analisador léxico ou sintatico:
  
``python analisador_lexico.py``
``python analisador_sintatico.py``


  4. Digite o nome do arquivo de texto que deseja analisar quando solicitado.

  5. Os tokens identificados serão exibidos no terminal.

## Exemplos

- [exemplo_lexico.txt](exemplo_lexico.txt): exemplo de arquivo de texto válido sem erros léxicos.
- [exemplo_erro_lexico.txt](exemplo_erro_lexico.txt): exemplo de arquivo de texto com erros léxicos.

## Sintatico 

Sintatico - Compilador simples desenvolvido em Python que realiza a análise sintaica de duas frases exemplos Frase1 ``'true'`` Frase2``false``de gramática e tabela shift-reduce simplificada.

## Funcionalidades da Frase1

A frase1 é: 'programa a ; begin a ; end'

Passo a passo da análise sintática:

- Pilha: [0] Entrada: ['programa', 'a', ';', 'begin', 'a', ';', 'end', '$']
- Estado atual: 0 Símbolo atual: 'programa'
- Ação: 's1' (deslocar para o estado 1)
- Pilha: [0, 'programa', 1] Entrada: ['a', ';', 'begin', 'a', ';', 'end', '$']
- Estado atual: 1 Símbolo atual: 'a'
- Ação: 's2' (deslocar para o estado 2)
- Pilha: [0, 'programa', 1, 'a', 2] Entrada: [';', 'begin', 'a', ';', 'end', '$']
- Estado atual: 2 Símbolo atual: ';'
- Ação: 's3' (deslocar para o estado 3)
- Pilha: [0, 'programa', 1, 'a', 2, ';', 3] Entrada: ['begin', 'a', ';', 'end', '$']
- Estado atual: 3 Símbolo atual: 'begin'
- Ação: 's4' (deslocar para o estado 4)
- Pilha: [0, 'programa', 1, 'a', 2, ';', 3, 'begin', 4] Entrada: ['a', ';', 'end', '$']
- Estado atual: 4 Símbolo atual: 'a'
- Ação: 's2' (deslocar para o estado 2)
- Pilha: [0, 'programa', 1, 'a', 2, ';', 3, 'begin', 4, 'a', 2] Entrada: [';', 'end', '$']
- Estado atual: 2 Símbolo atual: ';'
- Ação: 's3' (deslocar para o estado 3)
- Pilha: [0, 'programa', 1, 'a', 2, ';', 3, 'begin', 4, 'a', 2, ';', 3] Entrada: ['end', '$']
- Estado atual: 3 Símbolo atual: 'end'
- Ação: 'r3' (reduzir usando a regra 3)
- Pilha: [0, 'programa', 1, 'a', 2, ';', 3, 'begin', 4, '<sentencas>'] Entrada: ['end', '$']
- Estado atual: 0 Símbolo atual: '<sentencas>'
- Ação: 's5' (deslocar para o estado 5)
- Pilha: [0, 'programa', 1, 'a', 2, ';', 3, 'begin', 4, '<sentencas>', 5] Entrada: ['end', '$']
- Estado atual: 5 Símbolo atual: 'end'
- Ação: 'r3' (reduzir usando a regra 3)
- Pilha: [0, 'programa', 1, 'a', 2, ';', 3, 'begin', 4, '<sentencas>', 5, '<sentencas>'] Entrada: ['end', '$']
- Estado atual: 5 Símbolo atual: 'end'
- Ação: 'r3' (reduzir usando a regra 3)
- Pilha: [0, 'programa', 1, 'a', 2, ';', 3, 'begin', 4, '<sentencas>', 5, '<sentencas>'] Entrada: ['end', '$']
- Estado atual: 5 Símbolo atual: 'end'
- Ação: 'r3' (reduzir usando a regra 3)
- Pilha: [0, 'programa', 1, 'a', 2, ';', 3, 'begin', 4, '<sentencas>', 5, '<sentencas>'] Entrada: ['end', '$']
- Estado atual: 5 Símbolo atual: 'end'
- Ação: 'r3' (reduzir usando a regra 3)
- Pilha: [0, 'programa', 1, 'a', 2, ';', 3, 'begin', 4, '<sentencas>'] Entrada: ['end', '$']
- Estado atual: 4 Símbolo atual: 'end'
- Ação: 'r5' (reduzir usando a regra 5)
- Pilha: [0, 'programa', 1, 'a', 2, ';', 3, 'begin', '<corpo>'] Entrada: ['end', '$']
- Estado atual: 0 Símbolo atual: '<corpo>'
- Ação: 's6' (deslocar para o estado 6)
- Pilha: [0, 'programa', 1, 'a', 2, ';', 3, 'begin', '<corpo>', 6] Entrada: ['end', '$']
- Estado atual: 6 Símbolo atual: 'end'
- Ação: 'r5' (reduzir usando a regra 5)
- Pilha: [0, 'programa', 1, 'a', 2, ';', 3, '<corpo>'] Entrada: ['end', '$']
- Estado atual: 0 Símbolo atual: '<corpo>'
- Ação: 's6' (deslocar para o estado 6)
- Pilha: [0, 'programa', 1, 'a', 2, ';', 3, '<corpo>', 6] Entrada: ['end', '$']
- Estado atual: 6 Símbolo atual: 'end'
- Ação: 'r5' (reduzir usando a regra 5)
- Pilha: [0, 'programa', 1, 'a', 2, ';', 3, '<corpo>'] Entrada: ['end', '$']
- Estado atual: 0 Símbolo atual: '<corpo>'
- Ação: 's6' (deslocar para o estado 6)
- Pilha: [0, 'programa', 1, 'a', 2, ';', 3, '<corpo>', 6] Entrada: ['end', '$']
- Estado atual: 6 Símbolo atual: 'end'
- Ação: 'r5' (reduzir usando a regra 5)
- Pilha: [0, 'programa', 1, 'a', 2, ';', 3, '<corpo>'] Entrada: ['end', '$']
- Estado atual: 0 Símbolo atual: 'programa'
- Ação: 'r1' (reduzir usando a regra 1)
- Pilha: [0, '<programa>'] Entrada: ['end', '$']
- Estado atual: 0 Símbolo atual: '<programa>'
- Ação: 'accept' (aceitação)


## Referência

Compiladores 2a edição - Princípios, técnicas e ferramentas.- Alfred V. Aho Monica S. Lam Ravi Sethi Jeffrey D. Ullman
