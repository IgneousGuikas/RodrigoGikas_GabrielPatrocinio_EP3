# lista para facilitar doctest
lista_alimentos = ['ABACATE,100,177.00,1.80,6.40,16.00',
                   'ABACAXI,100,58.00,0.40,13.70,0.20',
                   'ABACAXI EM CALDA,100,122.00,0.44,29.77,0.18']

# lista para facilitar doctest
lista_usuario = ['Fulano da Silva,30,70,M,1.64,alto',
                 '06/04/15,IOGURTE,40',
                 '07/04/15,MACARRAO AO ALHO E OLEO,200',
                 '06/04/15,MAMAO PAPAYA,50']



    
def processa_dados_alimentos(lista_alimentos):
    '''
    Recebe a lista de linhas do arquivo 'alimentos.csv' e devolve
    um dicionário com alimentos como keys e valores nutricionais
    como values na forma de listas
    '''
    
    
    ''' Testa se processa_dados_alimentos funciona adequadamente
        >>> processa_dados_alimentos(lista_alimentos) == {'ABACATE': [100.0, 177.00, 1.80, 6.40, 16.00], 'ABACAXI': [100.0, 58.00, 0.40, 13.70, 0.20], 'ABACAXI EM CALDA': [100.0, 122.00, 0.44, 29.77, 0.18]}
        True
    '''
    catalogo = dict()
    for termo in lista_alimentos:
        valores = []
        linha = []
        linha = termo.split(',')
        for numero in linha[1:]:
            valores.append(float(numero))
        catalogo[linha[0]] = valores
    return catalogo

    
def processa_dados_usuario(lista_usuario):
    '''
    Recebe a lista de linhas do arquivo 'usuario.csv' e devolve
    um dicionário com as especificações do usuário e um dicionário
    com os alimentos ingeridos pelo usuário e suas quantidades
    '''
    
    
    ''' Testa se processa_dados_usuario funciona adequadamente
        >>> a = {}
        >>> b = {}
        >>> a,b = processa_dados_usuario(lista_usuario)
        >>> a == {'ALTURA': 1.64, 'NOME': 'Fulano da Silva', 'PESO': 70, 'SEXO': 'M', 'IDADE': 30, 'FATOR': 'alto'}
        True
        >>> b == {'06/04/15': ('IOGURTE', 40, 'MAMAO PAPAYA', 50), '07/04/15': ('MACARRAO AO ALHO E OLEO', 200)}
        True
        '''
    middle = lista_usuario[0].split(',')
    info_usuario = {'NOME': middle[0], 'IDADE': int(middle[1]), 'PESO': int(middle[2]), 'SEXO': middle[3], 'ALTURA': float(middle[4]), 'FATOR': middle[5]}
    consumo_semana = dict()
    for termo in lista_usuario[1:]:
         linha = []
         linha = termo.split(',')
         if linha[0] in consumo_semana:
             consumo_semana[linha[0]] += (linha[1], int(linha[2]))
         else:
             consumo_semana[linha[0]] = (linha[1], int(linha[2]))
    return info_usuario,consumo_semana
