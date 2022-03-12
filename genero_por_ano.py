import re
import csv
import sys



def html_genero_por_ano(genero_por_ano):
    f_html = open("distro_por_genero.html","w")
    f_html.write('''<!doctype html>
<html>
  <head>
    <title>Distribuição por género em cada ano e no total</title>
    <meta charset="utf-8">
  </head>
  <body>
  <h1> Distribuição por género em cada ano e no total </h1>''')
    for key in sorted(genero_por_ano):
      tuplo = genero_por_ano[key]
      f_html.write("<p>" + "Em " + key + ", " + str(tuplo[0] + tuplo[1]) + " atletas realizaram exame médico desportivo, sendo "+ str(tuplo[0]) + " do sexo feminino e " + str(tuplo[1]) + " do sexo masculino. " + "</p> \n")
    f_html.write('''    <a href="index.html">Volar à pagina inicial aqui</a> <br>
  </body>
</html>''')


def genero_por_ano(file):
    regex_ano    = r'\d{4}(?=-)'
    regex_genero = r'(F,|M,)'
    thisdict = {}
    for line in file:
      l = ','.join(line)
      m_genero = re.search(regex_genero,l)
      m_ano    = re.search(regex_ano,l)
      if m_ano and m_genero:
        ano = m_ano.group()
        if thisdict.get(ano):
          if m_genero.group() == "F,":
            tuplo    = thisdict[ano]
            tuplo[0] = tuplo[0] + 1
            thisdict.setdefault(ano,tuplo)
          if m_genero.group() == 'M,':
            tuplo    = thisdict[ano]
            tuplo[1] = tuplo[1] + 1
            thisdict.setdefault(ano,tuplo)
        else:
          if m_genero.group() == "F,":
            thisdict[ano] = [1,0]
          if m_genero.group() == 'M,':
            thisdict[ano] = [0,1]
      html_genero_por_ano(thisdict)

                
