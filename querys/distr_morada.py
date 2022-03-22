def html_info_utilizada(sortedList):
    f_html = open("html_code/distr_morada.html","w")
    f_html.write('''<!doctype html>
<html>
  <head>
    <title>Informação utilizada para calcular distribuição por morada</title>
    <meta charset="utf-8">
  </head>
  <body>
  <h1> Informação utilizada para calcular distribuição por morada </h1>\n<br>\n''')
    f_html.write("")
    for tuplo in sortedList:
        f_html.write("<h4>&nbsp;&nbsp;&nbsp;" + tuplo[0] + ": </h4>\n")
        for atleta in tuplo[1]:
            f_html.write("<p>&nbsp;&nbsp;&nbsp;" + atleta + " </p>\n" )
    f_html.write('''    <br> <a href="index.html">Voltar à pagina inicial aqui</a> <br>
  </body>
</html>''')


def distr_morada_index(lengthDict):
    f_html = open("html_code/index.html","a")
    f_html.write('''        <h2> &nbsp;&nbspDistribuição por morada </h2>\n''')
    for key in lengthDict:
        if key == 1:
            f_html.write('''          <p>  &nbsp;&nbsp &nbsp;&nbsp &nbsp;&nbsp;Existem ''' + str(len(lengthDict[key])) + " moradas onde habitam 1 atleta.</p>\n")
        else:
            f_html.write('''          <p>  &nbsp;&nbsp &nbsp;&nbsp &nbsp;&nbsp;Existem ''' + str(len(lengthDict[key])) + " moradas onde habitam " + str(key) + " atletas.</p>\n")
    f_html.write('''        <a href="distr_morada.html">Mais informação aqui</a> <br>\n''')  


def lengthDictionary(dict):
    newDict = {}
    for key in dict:
        length = len(dict[key])
        if length in newDict:
            newDict[length].append(key)
        else:
            newDict[length] = [key]

    return newDict


def distr_morada(atletas):
    moradaDict = {}

    for atleta in atletas:
        nome = atleta['Primeironome'] + ' ' + atleta['Ultimonome']
        if atleta['Morada'] in moradaDict.keys():
            moradaDict[atleta['Morada']].append(nome)
        else:
            moradaDict[atleta['Morada']] = [nome]

    for key in moradaDict:
        s = sorted(moradaDict[key], key=lambda tup: tup[0])
        moradaDict[key] = s
    sortedList = sorted(moradaDict.items(), key=lambda x: x[0])

    lengthDict = lengthDictionary(moradaDict)
    html_info_utilizada(sortedList)
    return lengthDict