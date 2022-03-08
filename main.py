
import sys
import re
import csv

# cabeçalho _id, index, dataEMD, nome/primeiro, nome/último, idade, género, morada, modalidade, clube, email, federado, resultado
# separador: ','

regex_emd  = r'(?P<id>\w+),(?P<index>\d+),'
p_emd = re.compile(regex_emd)

with open('emd.csv', mode = 'r') as file:
    ficheiro = csv.reader(file)
    for linha in ficheiro:
        for token in linha:
            mEmd = p
