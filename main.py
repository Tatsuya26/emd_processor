import re
import csv
import querys.genero_por_ano
import querys.modalidade_por_ano
import querys.datas_extremas
import querys.idade_e_genero
import querys.distr_morada
from querys.aptos_por_ano import aptos_por_ano
from querys.federado_por_ano import federado_por_ano

# cabeçalho _id, index, dataEMD, nome/primeiro, nome/último, idade, género, morada, modalidade, clube, email, federado, resultado
# separador: ','

def html_cabecalho(filename):
    f_html = open(filename,"w")
    f_html.write('''
<!doctype html>
<html>
    <head>
        <title>Exames Médicos Desportivos</title>
        <meta charset="utf-8">
    </head>
    <body>
        <h1> Exames Médicos Desportivos </h1>\n''')
    f_html.close()


def init_html(filename,queryA,queryB,queryC,queryD,queryE):
    html_cabecalho(filename)
    querys.datas_extremas.datas_extremas_to_index(queryA)
    querys.genero_por_ano.genero_por_ano_index(queryB)
    querys.modalidade_por_ano.modalidade_por_ano_index(queryC)
    querys.idade_e_genero.idade_e_genero_index(queryD)
    querys.distr_morada.distr_morada_index(queryE)
    #!!!!!!!!!!!!!!!!!!!!!!!!!:Colocar aqui funções que escrevem no index.html -> ver exemplos acima
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    f_html = open(filename,"a")
    f_html.write('''<h2>&nbsp;&nbsp;Distribuição por estatuto de federado em cada ano</h2>\n
        <a href="html_code/distro_federeado_ano.html">Distribuição por estatuto de federado em cada ano</a> <br>

            <h2>&nbsp;&nbsp;Percentagem de aptos e não aptos por ano</h2>\n            
        <a href="html_code/percentagem_aptos_nao_aptos_ano.html">Percentagem de aptos e não aptos por ano</a> <br>''')
    f_html.close()
    close_html()
    
def close_html():
    f_html = open('html_code/index.html',"a")
    f_html.write('''
    </body>
</html>''')
    f_html.close()


def initDict():
    f = open('dataset/emd.csv', mode = 'r')
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
    query_A = querys.datas_extremas.data_extremas(atletas)
    query_B = querys.genero_por_ano.genero_por_ano(atletas)
    query_C = querys.modalidade_por_ano.modalidade_por_ano(atletas)
    query_D = querys.idade_e_genero.idade_e_genero(atletas)
    query_E = querys.distr_morada.distr_morada(atletas)
    init_html("html_code/index.html",query_A ,query_B, query_C, query_D, query_E)
    #federado_por_ano(atletas)
    #aptos_por_ano(atletas)
    close_html()
    
main()