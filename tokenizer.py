import re
import csv
import ply.lex as lex

# cabeçalho _id, index, dataEMD, nome/primeiro, nome/último, idade, género, morada, modalidade, clube, email, federado, resultado
tokens = [
    'ID',
    'INDEX',
    'DATAEMD',
    'PRIMEIRONOME',
    'SEGUNDONOME',
    'GENERO',    
    'MORADA',    
    'MODALIDADE',
    'CLUBE',     
    'EMAIL',     
    'FEDERADO',  
    'RESULTADO', 
    'ERRO'
]

def t_ID(t):
    r'\w+'
    return t

def t_INDEX(t):
    r'\d+'
    return t

def t_DATAEMD(t):
    r'\d{4}-\d{2}-\d{2}'
    return t

def t_PRIMEIRONOME(t):
    r'[A-Za-z]'
    return t

def t_SEGUNDONOME(t):
    r'[A-Za-z]'
    return t

def t_IDADE(t):
    r'\d{1,2}'
    return t

def t_GENERO(t):
    r'(F|M)'
    return t

def t_MORADA(t):
    r'\b[A-Za-z]+\b'
    return t

def t_MODALIDADE(t):
    r'\b[A-Za-z]+\b'
    return t

def t_CLUBE(t):
    r'\b[A-Za-z]+\b'
    return t

def t_EMAIL(t):
    r'\b[A-Za-z\.]+@[A-Za-z]+\.[A-Za-z]+\b'
    return t

def t_FEDERADO(t):
    r'true|false'
    return t

def t_RESULTADO(t):
    r'true|false'
    return t

def t_error(t):
    print("ERROR: Ilegal character")
    t.lexer.skip(1)

t_ignore = '\n\t '

lexer = lex.lex()

with open('emd.csv', mode = 'r') as file:
    ficheiro = csv.reader(file)
    for line in ficheiro:
        for parcela in line:
            lexer.input(parcela)
            for token in lexer:
                print(token)
            
