import re
trueRegex = r'[Tt][Rr][Uu][Ee]'

def aptos_por_ano(atletas):
    dicAptoAno = {}
    dicNAptoAno = {}
    index = open('index.html','a')
    index.write('''
        <h2> 7.Aptos por ano </h2>
        <a href="percentagem_aptos_nao_aptos_ano.html">Dados de aptos e não aptos por ano</a>''')
    for dic in atletas:
        ano = re.split(r'-',dic['Data'])[0]
        if ano not in dicAptoAno.keys():
            dicAptoAno[ano] = 0
        if ano not in dicNAptoAno.keys():
            dicNAptoAno[ano] = 0
        fed = dic['Resultado']
        m = re.match(trueRegex,fed)
        if m:
            dicAptoAno[ano] += 1
        else:
            dicNAptoAno[ano] += 1
    for key in dicAptoAno.keys():
        numeroAtletasAno = dicAptoAno[key] + dicNAptoAno[key]
        percentagemAptoAno = '{:.2f}'.format(float(dicAptoAno[key] / numeroAtletasAno))
        percentagemNAptoAno = '{:.2f}'.format(float(dicNAptoAno[key] / numeroAtletasAno))
        index.write(f'''
        <p> ANO:{key} -> Atletas {numeroAtletasAno} onde {dicAptoAno[key]} estao aptos e {dicNAptoAno[key]} nao estao aptos;
        Percentagem de aptos {percentagemAptoAno} %; Percentagem de nao aptos {percentagemNAptoAno} % </p>''')
    index.close()
        