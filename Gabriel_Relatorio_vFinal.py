# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 12:25:53 2015

@author: Pipo
"""
#-----------------------------------------------------
'''String definidas para cada faixa de IMC em que o usuário se encontra,
mais a frente usaremos cada uma delas dependendo do resultado final do usuário,
o projeto foi feito desta maneira para que fosse possivel utilizar apenas uma
mensagem de erro e deixar o código mais limpo.'''

magreza_grave='''Você está em um estado crítico de magreza e deve procurar
                 urgentemente uma nutricionista para acompanhar-lhe um
                 tratamento.'''
magreza_moderada='''Você está quase em estado crítico de magreza, procure
                    uma nutricionista o mais rápido possível para realizar
                    um acompanhamento em sua dieta.'''
magreza_leve='''Vale lembrar que ao contrário do que se pensa, estar magro não indica que
                você está realmente saudável, recomenda-se fortemente que você procure
                uma nutricionista para que ela possa indicar-lhe uma dieta adequada para
                sua faixa de peso.'''
normal='''Vale lembrar que mesmo assim recomenda-se uma nutricionista para 
          acompanhar sua dieta.'''
sobrepeso='''Recomenda-se fortemente que você procure uma nutricionista para que ela
             possa lhe indicar uma dieta adequada para sua faixa de peso.'''
obeso_I='''Você já alcançou a obesidade, deve procurar uma nutricionista para realizar
           uma dieta adequada.'''
obeso_II='''Você está em no segundo grau de obesidade e deve procurar rápidamente uma
            nutricionista,para realizar uma dieta adequada!'''
obeso_III='''Você está no ultimo grau de obesidade, deve urgentemente procurar ajuda
             de uma nutricionista. Você necessita de acompanhamento médico para que
             possa chegar a um peso saudável.'''
             
''' Lista com as faixas de IMC declaradas acima'''
IMC_faixas = [magreza_grave, magreza_moderada, magreza_leve, normal, sobrepeso, obeso_I, obeso_II, obeso_III]
#--------------------------------------------------------
#Procura a faixa de IMC que o usuário se encontra e prepara parte do relatório baseado nisso.
def FAIXA_IMC(IMC,faixas_IMC=IMC_faixas):
    '''
    >>> FAIXA_IMC(21)
    ('saudável', 'normal')
    '''
    if IMC <=16:
        RESULTADO="no estado de magreza grave"
        REL_FINAL=faixas_IMC[0]
    elif 16 < IMC <= 17:
        RESULTADO="em estado de magreza moderada"
        REL_FINAL=faixas_IMC[1]
    elif 17 < IMC <= 18.5:
        RESULTADO="em estado de magreza leve"
        REL_FINAL=faixas_IMC[2]
    elif 18.5 < IMC <= 25:
        RESULTADO="saudável"
        REL_FINAL=faixas_IMC[3]
    elif 25< IMC <= 30:
        RESULTADO="com sobrepeso"
        REL_FINAL=faixas_IMC[4]
    elif 30< IMC <=35:
        RESULTADO="em estado de Obesidade Grau I"
        REL_FINAL=faixas_IMC[5]
    elif 35< IMC <=40:
        RESULTADO="em estado de Obesidade Grau II"
        REL_FINAL=faixas_IMC[6]
    elif IMC > 40:
        RESULTADO="em estado de Obesidade Grau III"
        REL_FINAL=faixas_IMC[7]
    return RESULTADO,REL_FINAL
    #------------------------------------------------------------
'''Verifica se a Média diaria de calorias ingeridas é maior ou menor que o recomendado e prepara
    parte do relatório baseado nisso.'''
def CALCULA_COMPARACAO(total,calorias_diarias,dias):
    '''
    >>> CALCULA_COMPARACAO(700,600,2)
    'a menos que o'
    >>> CALCULA_COMPARACAO(1300,600,2)
    'a mais que o'
    >>> CALCULA_COMPARACAO(1200,600,2)
    ',exatamente igual o'
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
#----------------------------------------------------------------------------
    
#Cria um arquivo txt chamado "Relatório Final" com as especificações do usuário: 
relatorio_final=open("Relatório Final.txt","w",encoding="utf-8")
relatorio_final.writelines('''De acordo com sua dieta e seus dados, calculei que seu IMC é %3.2f,
isto indica que você está %s. Percebi também que você está
ingerindo, em média %3.2f calorias %s recomendado,o que resultou %s de %3.2f gramas. %s''' % (IMC,RESULTADO,MEDIA_CAL,COMPARACAO,DIFERENCA,quantidade,REL_FINAL)
relatorio_final.close()
