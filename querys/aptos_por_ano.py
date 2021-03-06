import re
trueRegex = r'[Tt][Rr][Uu][Ee]'

def orderNome(e):
    return e['Primeironome'] + ' ' + e['Ultimonome']

def html_info_utilizada(tuplo):
    f_html = open("html_code/distro_aptos_por_anos.html","w")
    f_html.write('''<!doctype html>
<html>
  <head>
    <title>Informação utilizada para calcular distribuição dos atletas federados por ano</title>
    <meta charset="utf-8">
  </head>
  <body>
  <h1> Informação utilizada para calcular distribuição dos atletas federados por ano</h1>\n<br>\n''')
    dicAptoAno = tuplo[0]
    dicNAptoAno = tuplo[1]
    for ano in sorted(dicAptoAno.keys()):
        f_html.write("<br>\n")
        f_html.write(f'''
            <table>
            <caption> <b>Atletas considerados aptos no ano {ano}</b> <caption>
                <tr>
                    <th>Nome do atleta</th>
                    <th>Data do exame médico</th>
                    <th>Modalidade </th>
                    <th>Clube </th>
                </tr>''')
        for atleta in dicAptoAno[ano]:
            f_html.write(f'''
                <tr>
                    <td>{atleta['Primeironome']} {atleta['Ultimonome']} </td>
                    <td>{atleta['Data']} </td>
                    <td>{atleta['Modalidade']}</td>
                    <td>{atleta['Clube']}</td>
                </tr>\n''' )
        f_html.write('            </table>')
        f_html.write("<br>\n")
        f_html.write(f'''
            <table>
            <caption> <b>Atletas federados no ano {ano}</b> <caption>
                <tr>
                    <th>Nome do atleta</th>
                    <th>Data do exame médico</th>
                    <th>Modalidade </th>
                    <th>Clube </th>
                </tr>''')
        for atleta in dicNAptoAno[ano]:
            f_html.write(f'''
                <tr>
                    <td>{atleta['Primeironome']} {atleta['Ultimonome']} </td>
                    <td>{atleta['Data']} </td>
                    <td>{atleta['Modalidade']}</td>
                    <td>{atleta['Clube']}</td>
                </tr>\n''' )
        f_html.write('            </table>')
    f_html.write('''    <br> <a href="index.html">Voltar à pagina inicial aqui</a> <br>
  </body>
</html>''')

def aptos_por_ano_to_index(tuplo):
    dicAptosAno = tuplo[0]
    dicNAptosAno = tuplo[1]
    index = open('html_code/index.html','a')
    index.write('''        <h2> &nbsp;&nbspPercentagem de aptos e não aptos por ano </h2>\n''')
    for ano in sorted(dicAptosAno.keys()):
        numeroAtletasAptos =len(dicAptosAno[ano])
        numeroAtletasNAptos = len(dicNAptosAno[ano])
        numeroAtletasAno = numeroAtletasAptos + numeroAtletasNAptos
        percentagemAptosAno = "{:.2f}%".format(float(numeroAtletasAptos / numeroAtletasAno))
        percentagemNAptosAno = "{:.2f}%".format(float(numeroAtletasNAptos / numeroAtletasAno))
        index.write(f'          <p>  &nbsp;&nbsp &nbsp;&nbsp &nbsp;&nbsp;No ano de {ano} realizaram-se {numeroAtletasAno} exames médicos a atletas\n')
        index.write(f'          <p>  &nbsp;&nbsp &nbsp;&nbsp &nbsp;&nbsp;Desses {numeroAtletasAno}, {numeroAtletasAptos} apresentaram exames positivos enquanto {numeroAtletasNAptos} não estão aptos a competir</p>\n')
        index.write(f'          <p>  &nbsp;&nbsp &nbsp;&nbsp &nbsp;&nbsp;Percentagem dos aptos : {percentagemAptosAno}; Percentagem dos não aptos : {percentagemNAptosAno}</p>\n')
    index.write(f'        <a href="distro_aptos_por_anos.html">Mais informação aqui</a> <br>\n')  
    index.close()
    

def aptos_por_ano(atletas):
    dicAptoAno = {}
    dicNAptoAno = {}
    for dic in atletas:
        ano = re.split(r'-',dic['Data'])[0]
        if ano not in dicAptoAno.keys():
            dicAptoAno[ano] = []
        if ano not in dicNAptoAno.keys():
            dicNAptoAno[ano] = []
        fed = dic['Resultado']
        m = re.match(trueRegex,fed)
        if m:
            dicAptoAno[ano].append(dic)
        else:
            dicNAptoAno[ano].append(dic)
    for key in sorted(dicAptoAno.keys()):
        dicAptoAno[key].sort(key = orderNome)
        dicNAptoAno[key].sort(key = orderNome)
    html_info_utilizada((dicAptoAno,dicNAptoAno))
    return (dicAptoAno,dicNAptoAno)    
