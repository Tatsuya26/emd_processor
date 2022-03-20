import re



def parse_genero_por_ano(dict):
    genero_por_ano = {}
    for key in sorted(dict):
      genero_por_ano[key] = [len(dict[key]["Femenino"]),len(dict[key]["Masculino"])]
    return genero_por_ano;


def html_info_Utilizada(dict):
    f_html = open("html_code/info_distro_por_genero.html","w")
    f_html.write('''<!doctype html>
<html>
  <head>
    <title>Informação utilizada para calcular distribuição por género em cada ano e no total</title>
    <meta charset="utf-8">
  </head>
  <body>
  <h1> Informação utilizada para calcular distribuição por género em cada ano e no total </h1>\n''')
    for key in sorted(dict):
      f_html.write("<h2>" + "Atletas no ano " + key + ": </h2>\n" )
      for sexo in dict[key]:
        f_html.write("    <h2>" + "   Sexo " + sexo + ": </h2>\n")
        for atleta in sorted(dict[key][sexo]):
          f_html.write("      <p>" + atleta +"</p>\n")
    f_html.write('''    <a href="index.html">Volar à pagina inicial aqui</a> <br>
  </body>
</html>''')

def genero_por_ano_index(queryB):
    f_html = open("html_code/index.html","a")            
    f_html.write('''<h2> &nbsp;&nbsp;&nbspDistribuição por género em cada ano e no total </h2>\n''')
    #Query b
    for key in sorted(queryB):
      tuplo = queryB[key]
      f_html.write("            <p>&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp" + "Em " + key + ", " + str(tuplo[0] + tuplo[1]) + " atletas realizaram exame médico desportivo, sendo "+ str(tuplo[0]) + " do sexo feminino e " + str(tuplo[1]) + " do sexo masculino. " + "</p> \n")
    f_html.write('''        <a href="info_distro_por_genero.html">Mais informação aqui</a> <br>''')
    f_html.close()


def genero_por_ano(dicionario):
    regex_ano    = r'\d{4}(?=-)'
    thisdict     = {}
    for atleta in dicionario:
      ano = re.search(regex_ano,atleta["Data"]).group()
      genero = atleta["Genero"]
      nome = atleta["Primeironome"] + " " + atleta["Ultimonome"]
      if thisdict.get(ano):
        if(genero == "F"):
          if thisdict.get(ano).get("Femenino") == None:
            thisdict[ano]["Femenino"] = []
          thisdict[ano]["Femenino"].append(nome)
        else :
          if thisdict.get(ano).get("Masculino") == None:
            thisdict[ano]["Masculino"] = []
          thisdict[ano]["Masculino"].append(nome)
      else:
        thisdict[ano] = {}
        if(genero == "F"):
          thisdict[ano]["Femenino"] = [nome]
        else :
          thisdict[ano]["Masculino"] = [nome]
    html_info_Utilizada(thisdict)
    return parse_genero_por_ano(thisdict)
      

