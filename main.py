import sys
import re
import csv
import genero_por_ano
import modalidade_por_ano

# cabeçalho _id, index, dataEMD, nome/primeiro, nome/último, idade, género, morada, modalidade, clube, email, federado, resultado
# separador: ','

def init_html(filename,queryB,queryC):
    f_html = open(filename,"w")
    f_html.write('''
<!doctype html>
<html>
    <head>
        <title>Exames Médicos Desportivos</title>
        <meta charset="utf-8">
    </head>
    <body>
        <h1> Exames Médicos Desportivos </h1>
                <h2> &nbsp;&nbspDatas extermas dos registos no dataset </h2>
        <a href="html_code/datas_extermas_dos_registos.html">Mais informação aqui</a> <br>
        <h2> &nbsp;&nbsp;&nbspDistribuição por género em cada ano e no total </h2>\n''')
    #Query b
    for key in sorted(queryB):
      tuplo = queryB[key]
      f_html.write("            <p>&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp" + "Em " + key + ", " + str(tuplo[0] + tuplo[1]) + " atletas realizaram exame médico desportivo, sendo "+ str(tuplo[0]) + " do sexo feminino e " + str(tuplo[1]) + " do sexo masculino. " + "</p> \n")
    f_html.write('''        <a href="html_code/info_distro_por_genero.html">Mais informação aqui</a> <br>''')
    #Query c
    f_html.write("          <h2> &nbsp;&nbsp;Distribuição por modalidade em cada ano e no total </h2>\n")
    for ano in sorted(queryC):
        f_html.write("          <h3> &nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp" + "Em " + ano +":\n</h3>")
        for modalidade in sorted(queryC[ano]):
             f_html.write("<p> &nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;" + str(queryC[ano][modalidade]) + " atletas inscritos em " + modalidade + "\n</p>")
    f_html.write('''<a href="html_code/distro_por_modalidade.html">Mais informação aqui</a> <br>\n''')

    f_html.write(''' <h2>&nbsp;&nbsp; Distribuição por idade e género (para a idade, considera apenas 2 escalões: < 35 anos e >= 35) </h2>\n
        <a href="html_code/distro_por_idade_genero.html"> Distribuição por idade e género (para a idade, considera apenas 2 escalões: < 35 anos e >= 35)</a> <br>

            <h2>&nbsp;&nbsp;Distribuição por morada </h2>\n
        <a href="html_code/distro_morada.html">Distribuição por morada</a> <br>

            <h2>&nbsp;&nbsp;Distribuição por estatuto de federado em cada ano</h2>\n
        <a href="html_code/distro_federeado_ano.html">Distribuição por estatuto de federado em cada ano</a> <br>

            <h2>&nbsp;&nbsp;Percentagem de aptos e não aptos por ano</h2>\n            
        <a href="html_code/percentagem_aptos_nao_aptos_ano.html">Percentagem de aptos e não aptos por ano</a> <br>
    </body>
</html>''')

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
    query_B = genero_por_ano.genero_por_ano(atletas)
    query_C = modalidade_por_ano.modalidade_por_ano(atletas)
    init_html("html_code/index.html", query_B, query_C)
    
main()

