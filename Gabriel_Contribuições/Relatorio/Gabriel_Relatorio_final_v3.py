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
                 urgentemente uma nutricionista para acompanhá-la em um
                 tratamento.'''
magreza_moderada='''Você está quase em estado crítico de magreza, procure
                    uma nutricionista o mais rápido possível para realizar
                    um acompanhamento em sua dieta.'''
magreza_leve='''Vale lembrar que ao contrário do que se pensa, estar magro não indica que
                você está realmente saudável, recomenda-se fortemente que você precure
                uma nutricionista para que ela possa indicá-la uma dieta adequada para
                sua faixa de peso.'''
normal='''Vale lembrar que mesmo assim recomenda-se uma nutricionista para 
          acompanhar sua dieta.'''
sobrepeso='''Recomenda-se fortemente que você precure uma nutricionista para que ela
             possa indicá-la uma dieta adequada para sua faixa de peso.'''
obeso_I='''Você já alcançou a obesidade, deve procurar uma nutricionista para realizar
           uma dieta adequada.'''
obeso_II='''Você está em no segundo grau de obesidade e deve procurar rápidamente uma
            nutricionista,para realizar uma dieta adequada!'''
obeso_III='''Você está no ultimo grau de obesidade, deve urgentemente procurar ajuda
             de uma nutricionista. Você necessita de acompanhamento médico para que
             possa chegar a um peso saudável.'''

#--------------------------------------------------------
#Procura a faixa de IMC que o usuário se encontra e prepara parte do relatório baseado nisso.
def FAIXA_IMC(IMC):
    if IMC <=16:
        RESULTADO="no estado de magreza grave"
        REL_FINAL=magreza_grave
    elif 16 < IMC <= 17:
        RESULTADO="em estado de magreza moderada"
        REL_FINAL=magreza_moderada
    elif 17 < IMC <= 18.5:
        RESULTADO="em estado de magreza leve"
        REL_FINAL=magreza_leve
    elif 18.5 < IMC <= 25:
        RESULTADO="saudável"
        REL_FINAL=normal
    elif 25< IMC <= 30:
        RESULTADO="com sobrepeso"
        REL_FINAL=sobrepeso
    elif 30< IMC <=35:
        RESULTADO="em estado de Obesidade Grau I"
        REL_FINAL=obeso_I
    elif 35< IMC <=40:
        RESULTADO="em estado de Obesidade Grau II"
        REL_FINAL=obeso_II
    elif IMC > 40:
        RESULTADO="em estado de Obesidade Grau III"
        REL_FINAL=obeso_III
    return RESULTADO,REL_FINAL
    #------------------------------------------------------------
'''Verifica se a Média diaria de calorias ingeridas é maior ou menor que o recomendado e prepara
    parte do relatório baseado nisso.'''
def CALCULA_COMPARAÇÃO(calorias_ingeridas,RECOMENDADO,dias):
    MEDIA_CAL=sum(calorias_ingeridas)/(dias)
    if MEDIA_CAL < RECOMENDADO:
        COMPARAÇÃO="a menos que o"
    elif MEDIA_CAL > RECOMENDADO:
        COMPARAÇÃO="a mais que o"
    else:
        COMPARAÇÃO=",exatamente igual o"
    return COMPARAÇÃO

#------------------------------------------------------------
#função que calcula quanto o usuário ganhou ou perdeu de massa.
def ganho_ou_perda_massa(calorias_ingeridas,RECOMENDADO):
    ganho_ou_perda=RECOMENDADO-calorias_ingeridas
    if ganho_ou_perda <=0:
        #"Ingeriu mais que o recomendado, ganhará massa"
        peso_ganho= abs(ganho_ou_perda)/7
        DIFERENÇA="no ganho"
        quantidade=peso_ganho
    elif ganho_ou_perda>0:
        #"Ingeriu menos que o recomendado,perderá massa"
        peso_perdido=ganho_ou_perda/7
        quantidade=peso_perdido
        #"Você ingeriu o mesmo que foi recomendado, manterá o peso"
    return peso_ganho,peso_perdido,DIFERENÇA,quantidade
#----------------------------------------------------------------------------
    
#Cria um arquivo txt chamado "Relatório Final" com as especificações do usuário: 
relatorio_final=open("Relatório Final.txt","w",encoding="utf-8")
relatorio_final.writelines('''De acordo com sua dieta e seus dados, calculei que seu IMC é %3.2f,
isto indica que você está %s. Percebi também que você está
ingerindo, em média %3.2f calorias %s recomendado,o que resultou %s de %3.2f gramas. %s''' ) % (IMC,RESULTADO,MEDIA_CAL,COMPARAÇÃO_MEDIA,DIFERENÇA,quantidade,REL_FINAL)
relatorio_final.close()