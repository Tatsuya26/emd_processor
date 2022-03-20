from operator import mod


def distr_morada(atletas):
    moradaDict = {}

    for atleta in atletas:
        nome = atleta['Primeironome'] + ' ' + atleta['Ultimonome']
        modalidade = atleta['Modalidade']
        tuplo = (nome, modalidade)
        if atleta['Morada'] in moradaDict.keys():
            moradaDict[atleta['Morada']].append(tuplo)
        else:
            moradaDict[atleta['Morada']] = [tuplo]

    for key in moradaDict:
        s = sorted(moradaDict[key], key=lambda tup: tup[0])
        moradaDict[key] = s
    
    sortedDict = sorted(moradaDict.items(), key=lambda x: x[0])
    for i in range(0, len(sortedDict)):
        print(sortedDict[i])