def idade_e_genero(atletas):
    # lista[0] = F e < 35
    # lista[1] = F e >= 35
    # lista[2] = M e < 35
    # lista[3] = M e >= 35
    lista = [[], [], [], []]

    for atleta in atletas:
        nome = atleta['Primeironome'] + ' ' + atleta['Ultimonome']
        modalidade = atleta['Modalidade']
        idade = atleta['Idade']
        genero = atleta['Genero']
        tuplo = (nome, modalidade, idade)
        if genero == 'F':
            if int(idade) < 35:
                lista[0].append(tuplo)
            else:
                lista[1].append(tuplo)
        else:
            if int(idade) < 35:
                lista[2].append(tuplo)
            else:
                lista[3].append(tuplo)

    for i in range(0, len(lista)):
        l = sorted(lista[i], key=lambda x: (x[2], x[0]))
        for value in l:
            print(value)
        print()

