
def calcula_calorias_recomendadas(info_usuario):
    '''
    Recebe um dicionário com as informações do usuario e devolve
    uma variável com a quantidade recomendada de calorias ingeridas
    por dia para esse usuario
        
        
        Testa se calcula_calorias_recomendadas funciona adequadamente
        >>> calcula_calorias_recomendadas({'ALTURA': 1.64, 'NOME': 'Fulano da Silva', 'PESO': 70, 'SEXO': 'M', 'IDADE': 30, 'FATOR': 'alto'})
        2833.416
        '''
    # calcula a Taxa Metabólica Basal (TMB) baseado no sexo do usuario
    if info_usuario['SEXO'] == 'M':
        TMB = 88.36 + (13.4 * info_usuario['PESO']) + (4.8 * info_usuario['ALTURA'] * 100) - (5.7 * info_usuario['IDADE'])
    else:
        TMB = 447.6 + (9.2 * info_usuario['PESO']) + (3.1 * info_usuario['ALTURA'] * 100) - (4.3 * info_usuario['IDADE'])
    
    
    # calcula a quantidade recomendada de calorias a ser ingerida por dia (em kcal) segundo o TMB e o fator de atividade física
    if info_usuario['FATOR'] == 'mínimo':
        calorias_diarias = TMB * 1.2
    elif info_usuario['FATOR'] == 'baixo':
        calorias_diarias = TMB * 1.375
    elif info_usuario['FATOR'] == 'médio':
        calorias_diarias = TMB * 1.55
    elif info_usuario['FATOR'] == 'alto':
        calorias_diarias = TMB * 1.725
    else:
        calorias_diarias = TMB * 1.9
    
    return calorias_diarias



def calcula_IMC(info_usuario):
    '''
    Recebe um dicionário com as informações do usuário e devolve
    o índice de massa corporal (IMC) como um número
        
        
        Testa se indice_massa_corporal funciona adequadamente
        >>> calcula_IMC({'ALTURA': 1.64, 'NOME': 'Fulano da Silva', 'PESO': 70, 'SEXO': 'M', 'IDADE': 30, 'FATOR': 'alto'})
        26.42
        '''
    IMC = float('{0:.2f}'.format((1.3 * info_usuario['PESO'])/((info_usuario['ALTURA'])**2.5)))
    return IMC




def total_calorias_ingeridas(calorias_semana):
    '''
    Recebe um vetor com as calorias ingeridas pelo usuário por dia
    e devolve o número de dias listados e o total de calorias ingeridas
    pelo usuario
        
        
        Testa se total_calorias_ingeridas funciona adequadamente
        >>> total_calorias_ingeridas([296.9, 552.0])
        (2, 848.9)
        '''
    total = sum(calorias_semana)    
    dias = len(calorias_semana)
    return dias, total



'''Verifica se a Média diaria de calorias ingeridas é maior ou menor que o recomendado e prepara
    parte do relatório baseado nisso.'''
def CALCULA_COMPARACAO(total,calorias_diarias,dias):
    '''
    >>> CALCULA_COMPARACAO(700,600,2)
    ('a menos que o', 350.0)
    >>> CALCULA_COMPARACAO(1300,600,2)
    ('a mais que o', 650.0)
    >>> CALCULA_COMPARACAO(1200,600,2)
    (',exatamente igual o', 600.0)
    '''
    MEDIA_CAL=total/dias
    if MEDIA_CAL < calorias_diarias:
        COMPARACAO="a menos que o"
    elif MEDIA_CAL > calorias_diarias:
        COMPARACAO="a mais que o"
    else:
        COMPARACAO=",exatamente igual o"
    return COMPARACAO, MEDIA_CAL

#------------------------------------------------------------
#função que calcula quanto o usuário ganhou ou perdeu de massa.
def ganho_ou_perda_massa(total,calorias_diarias):
    '''
    >>> ganho_ou_perda_massa(1300, 600)
    ('no ganho', 100.0)
    >>> ganho_ou_perda_massa(200, 600)
    ('na perda', 57.142857142857146)
    '''
    ganho_ou_perda= calorias_diarias - total
    if ganho_ou_perda <=0:
        #"Ingeriu mais que o recomendado, ganhará massa"
        peso_ganho= abs(ganho_ou_perda)/7
        quantidade=peso_ganho
        DIFERENCA="no ganho"
    elif ganho_ou_perda>0:
        #"Ingeriu menos que o recomendado,perderá massa"
        DIFERENCA="na perda"
        peso_perdido=ganho_ou_perda/7
        quantidade=peso_perdido
        #"Você ingeriu o mesmo que foi recomendado, manterá o peso"
    return DIFERENCA,quantidade