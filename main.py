import sys
import re
import csv
from aptos_por_ano import aptos_por_ano
from federado_por_ano import federado_por_ano

# cabeçalho _id, index, dataEMD, nome/primeiro, nome/último, idade, género, morada, modalidade, clube, email, federado, resultado
# separador: ','

def init_html(filename):
    f_html = open(filename,"w")
    f_html.write('''<!doctype html>
<html>
    <head>
        <title>Exames Médicos Desportivos</title>
        <meta charset="utf-8">
    </head>
    <body>
        <h1> Exames Médicos Desportivos </h1>''')
    f_html.close()
    
def close_html():
    f_html = open('index.html',"a")
    f_html.write('''
    </body>
</html>''')
    f_html.close()

def initDict():
    f = open('emd.csv', mode = 'r')
    f = csv.reader(f)
    regex_emd = r'(?P<Id>\d{7}[A-Za-z0-9]{17}),(?P<Index>\d\d?),(?P<Data>\d{4}-\d{2}-\d{2}),(?P<Primeironome>[A-Z][a-z]+),(?P<Ultimonome>[A-Z][a-z]+),(?P<Idade>\d{1,2}),(?P<Genero>(M|F)),(?P<Morada>[A-Z][a-z]+),(?P<Modalidade>[A-Z][A-Za-zçãé]+),(?P<Clube>[A-Z][A-Za-zã]+),(?P<Email>[A-Za-z.]+[A-Za-z]+@[A-Za-z.ã]+[A-Za-z]),(?P<Federado>true|false),(?P<Resultado>true|false)'
    p_emd     = re.compile(regex_emd)
    atletas = []
    for line in f:
        l = ','.join(line)
        m_emd = re.search(regex_emd,l)
        if m_emd:
            dict = m_emd.groupdict()
            atletas.append(dict)
    return atletas


#Função principal que vai correr todas as funcionalidades e para cada uma criar o respetivo html e depois criar index.html como link geral para todas
def main():
    atletas = initDict()
    init_html("index.html")
    federado_por_ano(atletas)
    aptos_por_ano(atletas)
    close_html()
    
main()

