
import sys
import re
import csv
import genero_por_ano

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
        <h1> Exames Médicos Desportivos </h1>
        <p class="p-welcome">Welcome!</p>
        <a href="datas_extermas_dos_registos.html">Datas extermas dos registos no dataset</a> <br>
        <a href="distro_por_genero.html">Distribuição por género em cada ano e no total</a> <br>
        <a href="distro_por_modalidade.html">Distribuição por modalidade em cada ano e no total</a> <br>
        <a href="distro_por_idade_genero.html"> Distribuição por idade e género (para a idade, considera apenas 2 escalões: < 35 anos e >= 35)</a> <br>
        <a href="distro_morada.html">Distribuição por morada</a> <br>
        <a href="distro_federeado_ano.html">Distribuição por estatuto de federado em cada ano;</a> <br>
        <a href="percentagem_aptos_nao_aptos_ano.html">Percentagem de aptos e não aptos por ano</a> <br>
    </body>
</html>''')

#Função principal que vai correr todas as funcionalidades e para cada uma criar o respetivo html e depois criar index.html como link geral para todas
def main():
    f = open('emd.csv', mode = 'r')
    f = csv.reader(f)
    regex_emd = r"(?P<Id>\d{7}[A-Za-z0-9]{17}),(?P<Index>\d\d?),(?P<Data>\d{4}-\d{2}-\d{2}),(?P<Primeironome>[A-Z][a-z]+),(?P<Ultimonome>[A-Z][a-z]+),(?P<Idade>\d{1,2}),(?P<Genero>(M|F)),(?P<Morada>[A-Z][a-z]+),(?P<Modalidade>[A-Z][A-Za-zçãé]+),(?P<Clube>[A-Z][A-Za-zã]+),(?P<Email>[A-Za-z.]+[A-Za-z]+@[A-Za-z.ã]+[A-Za-z]),(?P<Federado>true|false),(?P<Resultado>true|false)"
    p_emd     = re.compile(regex_emd)
    print(regex_emd)
    atletas = []
    for line in f:
        l = ','.join(line)
        m_emd = re.search(regex_emd,l)
        if m_emd:
            dict = m_emd.groupdict()
            atletas.append(dict)
    print(atletas)
    init_html("index.html")
    
main()