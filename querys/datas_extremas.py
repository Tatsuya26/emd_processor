import re

def html_info_Utilizada(datas):
    f_html = open("html_code/datas_extermas_dos_registos.html","w")
    f_html.write('''<!doctype html>
<html>
  <head>
    <title>Informação utilizada para calcular distribuição por género em cada ano e no total</title>
    <meta charset="utf-8">
  </head>
  <body>
  <h1> Informação utilizada para calcular datas extermas dos registos </h1>\n''')
    f_html.write("Datas ordenadas de mais antiga para mais recente")
    for data in sorted(datas):
      f_html.write("<p>&nbsp;&nbsp;&nbsp;" + data + " </p>\n" )
    f_html.write('''    <a href="index.html">Volar à pagina inicial aqui</a> <br>
  </body>
</html>''')

def datas_extremas_to_index(datas):
    f_html = open("html_code/index.html","a")
    menordata = datas[0]
    maiordata = datas[len(datas) - 1]
    f_html.write('''        <h2> &nbsp;&nbspDatas extermas dos registos no dataset </h2>\n''')
    f_html.write('''          <p>  &nbsp;&nbsp &nbsp;&nbsp &nbsp;&nbsp;Exame médico mais antigo foi feito em:''' + menordata + ". </p>\n")
    f_html.write('''          <p>  &nbsp;&nbsp &nbsp;&nbsp &nbsp;&nbsp;Exame médico mais recente foi feito em:''' + maiordata + ".</p>\n")
    f_html.write('''        <a href="datas_extermas_dos_registos.html">Mais informação aqui</a> <br>\n''')  


    
def data_extremas(dict):
    datas = []
    for atleta in dict:
        datas.append(atleta["Data"] +", " + atleta["Primeironome"] + " " + atleta["Ultimonome"])
    datas.sort()
    html_info_Utilizada(datas)
    return datas
    




