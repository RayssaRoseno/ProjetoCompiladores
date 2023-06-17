# Compilador

Este é um compilador simples desenvolvido em Python que realiza a análise léxica de um arquivo de texto seguindo uma determinada gramática(BNF).

## Funcionalidades

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


  3. Execute o analisador léxico:
  
``python analisador_lexico.py``


  4. Digite o nome do arquivo de texto que deseja analisar quando solicitado.

  5. Os tokens identificados serão exibidos no terminal.

## Exemplos

- [exemplo_lexico.txt](exemplo_lexico.txt): exemplo de arquivo de texto válido sem erros léxicos.
- [exemplo_erro_lexico.txt](exemplo_erro_lexico.txt): exemplo de arquivo de texto com erros léxicos.


## Referência

Sessão 3: "O GERADOR DE ANALISADOR LÉXICO LEX". - Compiladores 2a edição - Princípios, técnicas e ferramentas.- Alfred V. Aho Monica S. Lam Ravi Sethi Jeffrey D. Ullman
