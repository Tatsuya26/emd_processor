def html_info_utilizada(sortedListas):
    f_html = open("html_code/idade_e_genero.html","w")
    f_html.write('''<!doctype html>
<html>
  <head>
    <title>Informação utilizada para calcular distribuição por idade e género</title>
    <meta charset="utf-8">
  </head>
  <body>
  <h1> Informação utilizada para calcular distribuição por idade e género </h1>\n''')
    f_html.write("")
    for i in range(0, len(sortedListas)):
        if i == 0:
            f_html.write("<h2>Sexo feminino: </h2>\n")
            f_html.write("<h3>Com menos de 35 anos: </h3>\n")
        elif i == 1:
            f_html.write("<h3>Com 35 ou mais anos: </h3>\n")
        elif i == 2:
            f_html.write("<br><h2>Sexo masculino: </h2>\n")
            f_html.write("<h3>Com menos de 35 anos: </h3>\n")
        else:
            f_html.write("<h3>Com 35 ou mais anos: </h3>\n")

        if i < 2:
            f_html.write('''
                <table>
                    <tr>
                        <th>Nome da atleta</th>
                        <th>Idade</th>
                    </tr>''')
        else:
            f_html.write('''
                <table>
                    <tr>
                        <th>Nome do atleta</th>
                        <th>Idade</th>
                    </tr>''')

        for atleta in sortedListas[i]:
            f_html.write(f'''
                <tr>
                    <td>{atleta[0]} </td>
                    <td>{atleta[1]} </td>
                </tr>\n''' )
        f_html.write('            </table>')
    f_html.write('''    <br> <a href="index.html">Voltar à pagina inicial aqui</a> <br>
  </body>
</html>''')


def idade_e_genero_index(listas):
    total_atletas = 0
    for lista in listas:
        total_atletas += len(lista)
    f_html = open("html_code/index.html","a")
    f_html.write('''        <h2> &nbsp;&nbspDistribuição por idade e género </h2>\n''')
    f_html.write(f'''          <p>  &nbsp;&nbsp &nbsp;&nbsp &nbsp;&nbsp; {str(len(listas[0]))} 
                                atletas do sexo feminino com menos de 35 anos ({"{:.2f}%".format(len(listas[0])/total_atletas)}).</p>\n''')
    f_html.write(f'''          <p>  &nbsp;&nbsp &nbsp;&nbsp &nbsp;&nbsp; {str(len(listas[1]))} 
                                atletas do sexo feminino com 35 anos ou mais anos ({"{:.2f}%".format(len(listas[1])/total_atletas)}).</p>\n''')
    f_html.write(f'''          <p>  &nbsp;&nbsp &nbsp;&nbsp &nbsp;&nbsp; {str(len(listas[2]))} 
                                atletas do sexo masculino com menos de 35 anos ({"{:.2f}%".format(len(listas[2])/total_atletas)}).</p>\n''')
    f_html.write(f'''          <p>  &nbsp;&nbsp &nbsp;&nbsp &nbsp;&nbsp; {str(len(listas[3]))} 
                                atletas do sexo masculino com 35 anos ou mais anos ({"{:.2f}%".format(len(listas[3])/total_atletas)}).</p>\n''')
    f_html.write('''        <a href="idade_e_genero.html">Mais informação aqui</a> <br>\n''')  

def idade_e_genero(atletas):
    # lista[0] = F e < 35
    # lista[1] = F e >= 35
    # lista[2] = M e < 35
    # lista[3] = M e >= 35
    listas = [[], [], [], []]

    for atleta in atletas:
        nome = atleta['Primeironome'] + ' ' + atleta['Ultimonome']
        idade = atleta['Idade']
        genero = atleta['Genero']
        tuplo = (nome, idade)
        if genero == 'F':
            if int(idade) < 35:
                listas[0].append(tuplo)
            else:
                listas[1].append(tuplo)
        else:
            if int(idade) < 35:
                listas[2].append(tuplo)
            else:
                listas[3].append(tuplo)

    for i in range(0, len(listas)):
        l = sorted(listas[i], key=lambda x: (x[1], x[0]))
        listas[i] = l

    html_info_utilizada(listas)
    return listas