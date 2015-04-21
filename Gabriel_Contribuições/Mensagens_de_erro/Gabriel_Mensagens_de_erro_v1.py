# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 09:36:15 2015

@author: Pipo
"""


# Reproduz uma mensagem de erro caso o fator de atividade fisica do usuário não seja um dos 5 indicados.
if info_usuario['FATOR'] != ("mínimo","baixo","médio","alto","muito alto"):
    print('''Desculpe mas verificamos um erro no seu arquivo de entrada, parece que
             seu fator de atividade física está em um padrão diferente, por favor 
             corrija para que possamos continuar,isto será importante para realizarmos os calculos''')
# Reproduz uma mensagem de erro caso a altura do usuário não seja um numero decimal.
if type(info_usuario['ALTURA']) != float:
    print('''Desculpe mas verificamos um erro no seu arquivo de entrada, parece que
             sua altura está em um padrão diferente, por favor 
             corrija para que possamos continuar,isto será importante para realizarmos os calculos''')
# Reproduz uma mensagem de erro caso a idade do usuario não seja um número inteiro.
if type(info_usuario['IDADE']) !=int:
    print('''Desculpe mas verificamos um erro no seu arquivo de entrada, parece que
             sua idade está em um padrão diferente, por favor 
             corrija para que possamos continuar,isto será importante para realizarmos os calculos''')    
# Reproduz uma mensagem de erro caso o nome do usuário tenha menos que 2 caracteres.
if len(info_usuario['NOME']) <= 1:
    print('''Desculpe mas verificamos um erro no seu arquivo de entrada, parece que
             seu nome não é válido, por favor 
             corrija para que possamos continuar''')  
# Reproduz uma mensagem de erro caso o sexo do usuário seja diferente de masculino ou feminino e homem ou mulher.
if (info_usuario['SEXO'])!=("homem","mulher","masculino","feminino"):
    print('''Desculpe mas verificamos um erro no seu arquivo de entrada, parece que
             seu sexo está em um padrão diferente, por favor 
             corrija para que possamos continuar,isto será importante para realizarmos os calculos''')
# Reproduz uma mensagem de erro caso algum alimento inserido não esteja na lista de alimentos.
print('''Desculpe, não foi possivel encontrar algum dos alimentos que você digitou, reveja sua lista
         antes de continuarmos.")



