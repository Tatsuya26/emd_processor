import re;

def html_info_utilizada(query):
    f_html = open("html_code/distro_por_modalidade.html","w")
    f_html.write('''<!doctype html>
<html>
  <head>
    <title>Informação utilizada para calcular distribuição por modalidade em cada ano e no total</title>
    <meta charset="utf-8">
  </head>
  <body>
  <h1> Informação utilizada para calcular distribuição por modalidade em cada ano e no total </h1>\n''')
    for ano in sorted(query):
        f_html.write("      <h2> Ano " + ano + ": </h2>\n")
        for modalidade in query[ano]:
            f_html.write("          <h3> &nbsp;&nbsp;&nbsp" + modalidade + " :</h3>\n")
            for atleta in sorted(query[ano][modalidade]):
                f_html.write("              <p> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" + atleta + "</p>\n")
    f_html.write('''    <a href="index.html">Volar à pagina inicial aqui</a> <br>
  </body>
</html>''')




def parse_modalide_por_ano(dict):
    new_dict = {}
    for ano in sorted(dict):
        new_dict[ano] = {}
        for modalidade in sorted(dict[ano]):
            new_dict[ano][modalidade] = len(dict[ano][modalidade])
    return new_dict




def modalidade_por_ano(dict):
    regex_ano = r'\d{4}(?=-)'
    query     = {}   
    for atleta in dict:
        modalide = atleta["Modalidade"]
        ano = re.search(regex_ano,atleta["Data"]).group()
        nome = atleta["Primeironome"] + " " + atleta["Ultimonome"] + ", " + atleta["Clube"]
        if query.get(ano):
            if query[ano].get(modalide) == None:
                query[ano][modalide] = []
            query[ano][modalide].append(nome)
        else:
            query[ano] = {}
            query[ano][modalide] = [nome]
    html_info_utilizada(query)
    return parse_modalide_por_ano(query)


def modalidade_por_ano_index(queryC):
    f_html = open("html_code/index.html","a")
    f_html.write("          <h2> &nbsp;&nbsp;Distribuição por modalidade em cada ano e no total </h2>\n")
    for ano in sorted(queryC):
        f_html.write("          <h3> &nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp" + "Em " + ano +":\n</h3>")
        for modalidade in sorted(queryC[ano]):
             f_html.write("<p> &nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;" + str(queryC[ano][modalidade]) + " atletas inscritos em " + modalidade + "</p>\n")
    f_html.write('''<a href="distro_por_modalidade.html">Mais informação aqui</a> <br>\n''')
    f_html.close()