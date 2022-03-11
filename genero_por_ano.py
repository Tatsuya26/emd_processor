import re
import csv
import sys



def html_genero_por_ano():
    f_html = open("distro_por_genero.html","w")
    f_html.write('''<!doctype html>
<html>
  <head>
    <title>Distribuição por género em cada ano e no total</title>
    <meta charset="utf-8">
  </head>
  <body>
    <p>Something<strong>body</strong></p>
    <a href="index.html">Volar à pagina inicial aqui</a> <br>
  </body>
</html>''')


#incompleta!!
def genero_por_ano(file):
    regex_idade  = r'\d{1,2}'
    regex_genero = r'(F|M)'

    dic = {"M":0,"F":0}
    for line in file:
        for token in line:
            m = re.search(regex_genero,token)
            if m.group:
                print(m.group())
                
html_genero_por_ano()
