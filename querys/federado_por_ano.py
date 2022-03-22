import re
trueRegex = r'[Tt][Rr][Uu][Ee]'

def orderNome(e):
    return e['Primeironome'] + ' ' + e['Ultimonome']

def federado_por_ano_to_index(tuplo):
    dicFed = tuplo[0]
    dicNFed = tuplo[1]
    index = open('html_code/index.html','a')
    index.write('''        <h2> &nbsp;&nbspDistribuição por estatuto de federado em cada ano </h2>\n''')
    for ano in dicFed.keys():
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
    return (dicFedAno,dicNFedAno)
        