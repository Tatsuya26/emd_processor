import re
trueRegex = r'[Tt][Rr][Uu][Ee]'

def orderNome(e):
    return e['Primeironome'] + ' ' + e['Ultimonome']

def html_info_utilizada(tuplo):
    f_html = open("html_code/distro_federado_por_anos.html","w")
    f_html.write('''<!doctype html>
<html>
  <head>
    <title>Informação utilizada para calcular distribuição dos atletas federados por ano</title>
    <meta charset="utf-8">
  </head>
  <body>
  <h1> Informação utilizada para calcular distribuição dos atletas federados por ano</h1>\n''')
    dicFedAno = tuplo[0]
    dicNFedAno = tuplo[1]
    for ano in sorted(dicFedAno.keys()):
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
        for atleta in dicFedAno[ano]:
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
            <caption> <b>Atletas não federados no ano {ano}</b> <caption>
                <tr>
                    <th>Nome do atleta</th>
                    <th>Data do exame médico</th>
                    <th>Modalidade </th>
                    <th>Clube </th>
                </tr>''')
        for atleta in dicNFedAno[ano]:
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

def federado_por_ano_to_index(tuplo):
    dicFed = tuplo[0]
    dicNFed = tuplo[1]
    index = open('html_code/index.html','a')
    index.write('''        <h2> &nbsp;&nbspDistribuição por estatuto de federado em cada ano </h2>\n''')
    for ano in sorted(dicFed.keys()):
        numeroAtletasFed =len(dicFed[ano])
        numeroAtletasNFed = len(dicNFed[ano])
        numeroAtletasAno = numeroAtletasFed + numeroAtletasNFed
        percentagemFedAno = "{:.2f}%".format(float(numeroAtletasFed / numeroAtletasAno))
        percentagemNFedAno = "{:.2f}%".format(float(numeroAtletasNFed / numeroAtletasAno))
        index.write(f'          <p>  &nbsp;&nbsp &nbsp;&nbsp &nbsp;&nbsp;No ano de {ano} realizaram-se {numeroAtletasAno} exames médicos a atletas\n')
        index.write(f'          <p>  &nbsp;&nbsp &nbsp;&nbsp &nbsp;&nbsp;Desses {numeroAtletasAno}, {numeroAtletasFed} são atletas federados enquanto {numeroAtletasNFed} não são federados</p>\n')
        index.write(f'          <p>  &nbsp;&nbsp &nbsp;&nbsp &nbsp;&nbsp;Percentagem dos federados : {percentagemFedAno}; Percentagem dos não federados : {percentagemNFedAno}</p>\n')
    index.write(f'        <a href="distro_federado_por_anos.html">Mais informação aqui</a> <br>\n')  
    index.close()
        
        
    

def federado_por_ano(atletas):
    dicFedAno = {}
    dicNFedAno = {}
    for dic in atletas:
        ano = re.split(r'-',dic['Data'])[0]
        if ano not in dicFedAno.keys():
            dicFedAno[ano] = []
        if ano not in dicNFedAno.keys():
            dicNFedAno[ano] = []
        fed = dic['Federado']
        m = re.match(trueRegex,fed)
        if m:
            dicFedAno[ano].append(dic)
        else:
            dicNFedAno[ano].append(dic)
    for key in sorted(dicFedAno.keys()):
        dicFedAno[key].sort(key = orderNome)
        dicNFedAno[key].sort(key = orderNome)
    html_info_utilizada((dicFedAno,dicNFedAno))
    return (dicFedAno,dicNFedAno)
        