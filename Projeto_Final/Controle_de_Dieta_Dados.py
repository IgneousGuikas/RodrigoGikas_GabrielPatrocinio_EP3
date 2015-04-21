from datetime import *

# lista para facilitar doctest
lista_alimentos = ['ABACATE,100,177.00,1.80,6.40,16.00',
                   'ABACAXI,100,58.00,0.40,13.70,0.20',
                   'ABACAXI EM CALDA,100,122.00,0.44,29.77,0.18']

# lista para facilitar doctest
lista_usuario = ['Fulano da Silva,30,70,M,1.64,alto',
                 '06/04/15,IOGURTE,40',
                 '07/04/15,MACARRAO AO ALHO E OLEO,200',
                 '06/04/15,MAMAO PAPAYA,50']

# dicionário para facilitar doctest
catalogo = {'PEIXE A MILANESA': [100.0, 266.0, 21.83, 14.8, 13.24],
            'MUCILON DE MILHO': [100.0, 381.0, 7.1, 85.7, 1.1],
            'CHEESEBURGUER': [100.0, 256.0, 16.08, 28.76, 8.5],
            'PRESUNTO': [100.0, 276.0, 16.7, 0.0, 23.2],
            "MILKSHAKE BAUNILHA PEQ MC DONALD'S": [100.0, 360.0, 11.0, 59.0, 9.0]}

# dicionário para facilitar doctest
consumo_semana = {'06/04/15': ('PEIXE A MILANESA', 40.0, 'MUCILON DE MILHO', 50.0),
                  '07/04/15': ('PRESUNTO', 200.0)}




def processa_dados_alimentos(lista_alimentos):
    '''
    Recebe a lista de linhas do arquivo 'alimentos.csv' e devolve
    um dicionário com alimentos como keys e valores nutricionais
    como values na forma de listas
        
        Testa se processa_dados_alimentos funciona adequadamente
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
        
        
        Testa se processa_dados_usuario funciona adequadamente
        >>> a = {}
        >>> b = {}
        >>> a,b = processa_dados_usuario(lista_usuario)
        >>> a == {'ALTURA': 1.64, 'NOME': 'Fulano da Silva', 'PESO': 70, 'SEXO': 'M', 'IDADE': 30, 'FATOR': 'alto'}
        True
        >>> b == {'06/04/15': ('IOGURTE', 40.0, 'MAMAO PAPAYA', 50.0), '07/04/15': ('MACARRAO AO ALHO E OLEO', 200.0)}
        True
        '''
    middle = lista_usuario[0].split(',')
    
    # cria dicionário com as informações do usuário
    info_usuario = {'NOME': middle[0], 'IDADE': int(middle[1]), 'PESO': int(middle[2]), 'SEXO': middle[3], 'ALTURA': float(middle[4]), 'FATOR': middle[5]}
    
    consumo_semana = dict()
    
    # cria dicionário com os dias listados pelo usuário como chaves e listas com os alimentos ingeridos intercalados com suas quantidades como valores
    for termo in lista_usuario[1:]:
         linha = []
         linha = termo.split(',')
         if linha[0] in consumo_semana:
             consumo_semana[linha[0]] += (linha[1], float(linha[2]))
         else:
             consumo_semana[linha[0]] = (linha[1], float(linha[2]))
    return info_usuario,consumo_semana



def pesquisa_alimentos(catalogo, consumo_semana):
    '''
    Recebe dois dicionários, um com o catálogo de alimentos e outro com
    o consumido pelo usuario na semana e devolve um vetor com as calorias
    ingeridas por dia e  outros vetores semelhantes para proteínas,
    carboidratos e gorduras
        
        
        Testa se pesquisa_alimentos funciona adequadamente
        >>> calorias = []
        >>> proteinas = []
        >>> carboidratos = []
        >>> gorduras = []   
        >>> lista_dias = []
        >>> erros = 0
        >>> lista_dias, erros, calorias, proteinas, carboidratos, gorduras = pesquisa_alimentos(catalogo, consumo_semana)
        >>> print(lista_dias)
        [datetime.date(15, 4, 6), datetime.date(15, 4, 7)]
        >>> print(erros)
        1
        >>> print(calorias)
        [296.9, 552.0]
        >>> print(proteinas)
        [12.282, 33.4]
        >>> print(carboidratos)
        [48.77, 0.0]
        >>> print(gorduras)
        [5.846, 46.4]
        >>> pesquisa_alimentos(catalogo, {'06/07/15': ('WASABI', 40.0)})
        ([], 0, [0], [0], [0], [0])
        '''
    calorias_semana = [0]*len(consumo_semana)
    proteinas_semana = [0]*len(consumo_semana)
    carboidratos_semana = [0]*len(consumo_semana)
    gorduras_semana = [0]*len(consumo_semana)
    
    erros = 1
    
    lista_dias = []
    
    modelo_ordem = sorted(consumo_semana)
    
    for dia in consumo_semana:
        porcoes = 0
        calorias = 0
        proteinas = 0
        carboidratos = 0
        gorduras= 0
        middle = dia.split('/')
        lista_dias.append(date(int(middle[2])+2000,int(middle[1]),int(middle[0])))
        
        for termo in range(0,len(consumo_semana[dia]),2):
            porcoes = 0
            
            # calcula os totais de calorias, proteínas, carboidratos e gorduras ingeridas pelo usuário por dia
            if consumo_semana[dia][termo] in catalogo:
                porcoes = float('{0:.4f}'.format((consumo_semana[dia][termo+1])/(catalogo[consumo_semana[dia][termo]][0]))) # calcula porções consumidas pelo usuario do alimento em função da porção padrão do catálogo                
                calorias += float('{0:.4f}'.format(catalogo[consumo_semana[dia][termo]][1] * porcoes)) # calcula consumo diario total de calorias
                proteinas += float('{0:.4f}'.format(catalogo[consumo_semana[dia][termo]][2] * porcoes)) # calcula consumo diario total de proteínas
                carboidratos += float('{0:.4f}'.format(catalogo[consumo_semana[dia][termo]][3] * porcoes)) # calcula consumo diario total de carboidratos
                gorduras += float('{0:.4f}'.format(catalogo[consumo_semana[dia][termo]][4] * porcoes)) # calcula consumo diario total de gorduras
            else:
                erros = 0
                lista_dias = []
        
        # insere os totais calculados acima em seu respectivo vetor em ordem crescente de dias da semana
        calorias_semana[modelo_ordem.index(dia)] = calorias
        proteinas_semana[modelo_ordem.index(dia)] = proteinas
        carboidratos_semana[modelo_ordem.index(dia)] = carboidratos
        gorduras_semana[modelo_ordem.index(dia)] = gorduras
    
    lista_dias = sorted(lista_dias)
    
    return lista_dias, erros, calorias_semana, proteinas_semana, carboidratos_semana, gorduras_semana
