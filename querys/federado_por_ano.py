import re
trueRegex = r'[Tt][Rr][Uu][Ee]'

def federado_por_ano(atletas):
    dicFedAno = {}
    dicNFedAno = {}
    index = open('index.html','a')
    index.write('''
        <h2> 6.Federados por ano </h2>
        <a href="percentagem_federados_nao_federados_ano.html">Dados de federados e não federados por ano</a>''')
    for dic in atletas:
        ano = re.split(r'-',dic['Data'])[0]
        if ano not in dicFedAno.keys():
            dicFedAno[ano] = 0
        if ano not in dicNFedAno.keys():
            dicNFedAno[ano] = 0
        fed = dic['Federado']
        m = re.match(trueRegex,fed)
        if m:
            dicFedAno[ano] += 1
        else:
            dicNFedAno[ano] += 1
    for key in dicFedAno.keys():
        numeroAtletasAno = dicFedAno[key] + dicNFedAno[key]
        percentagemFedAno = '{:.2f}'.format(float(dicFedAno[key] / numeroAtletasAno))
        percentagemNFedAno = '{:.2f}'.format(float(dicNFedAno[key] / numeroAtletasAno))
        index.write(f'''
        <p> ANO:{key} -> Atletas {numeroAtletasAno} onde {dicFedAno[key]} sao federados e {dicNFedAno[key]} nao sao federados;
        Percentagem de federados {percentagemFedAno} %; Percentagem de nao federados {percentagemNFedAno} % </p>''')
    index.close()
        