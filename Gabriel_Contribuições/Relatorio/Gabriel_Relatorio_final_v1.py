# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 12:25:53 2015

@author: Pipo
"""

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
    
print('''De acordo com sua dieta e seus dados, calculei que seu IMC é %3.2f,
         isto indica que você está %s. Percebi também que você está
         ingerindo, em média %3.2f calorias a %s que o recomendado. %s''' % (IMC,RESULTADO,MEDIA_CAL,COMPARAÇÃO_MEDIA,REL_FINAL))