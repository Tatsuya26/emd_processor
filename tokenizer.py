import re
import csv
import ply.lex as lex

# cabeçalho _id, index, dataEMD, nome/primeiro, nome/último, idade, género, morada, modalidade, clube, email, federado, resultado
states = (
    ('e2', 'exclusive'),
    ('e3', 'exclusive'),
    ('e4', 'exclusive'),
    ('e5', 'exclusive')
)


tokens = [
    'ID',
    'INDEX',
    'DATAEMD',
    'NOMEFIRST',
    'NOMELAST',
    'IDADE',
    'GENERO',    
    'MORADA',    
    'MODALIDADE',
    'CLUBE',     
    'EMAIL',     
    'FEDERADO',  
    'RESULTADO', 
    'ERRO'
]

# estado inicial

def t_GENERO(t):
    r'(F|M)'
    return t

def t_RESULTADO(t):
    r'true|false'
    return t
    
def t_ID(t):
    r'\d{7}[A-Za-z0-9]{17}'
    return t

def t_DATAEMD(t):
    r'\d{4}-\d{2}-\d{2}'
    return t

def t_INDEX(t):
    r'\d\d?'
    return t

def t_NOMEFIRST(t):
    r'[A-Z][a-z]+'
    t.lexer.begin('e2')
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ',\n\t '

def t_error(t):
    print("ERROR: Ilegal character")
    print(t.value)
    t.lexer.skip(1)



# estado 2

def t_e2_NOMELAST(t):
    r'[A-Z][a-z]+'
    return t

def t_e2_IDADE(t):
    r'\d{1,2}'
    return t

def t_e2_GENERO(t):
    r'(F|M)'
    t.lexer.begin('e3')
    return t



# estado 3

def t_e3_MORADA(t):
    r'[A-Z][a-z]+'
    t.lexer.begin('e4')
    return t



# estado 4

def t_e4_MODALIDADE(t):
    r'[A-Z][A-Za-z]+'
    t.lexer.begin('e5')
    return t



# estado 5

def t_e5_EMAIL(t):
    r'[A-Za-z.]+[A-Za-z]+@[A-Za-z.]+[A-Za-z]'
    return t

def t_e5_CLUBE(t):
    r'[A-Z][A-Za-z]+'
    return t

def t_e5_FEDERADO(t):
    r'true|false'
    t.lexer.begin('INITIAL')
    return t

t_ANY_ignore = ',\n\t '

def t_ANY_error(t):
    print("ERROR: Ilegal character")
    print(t.value)
    t.lexer.skip(1)

lexer = lex.lex()

with open('emd_test.csv', mode = 'r') as file:
    ficheiro = csv.reader(file)
    for line in ficheiro:
        for parcela in line:
            lexer.input(parcela)
            for token in lexer:
                print(token)
            
