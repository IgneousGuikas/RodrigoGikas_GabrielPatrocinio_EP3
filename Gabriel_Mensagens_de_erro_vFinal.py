# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 09:36:15 2015

@author: Pipo
"""


    # Reproduz uma mensagem de erro caso o fator de atividade fisica do usuário não seja um dos 5 indicados.
def MENSAGENS_ERROS(info_usuario):
    '''
    O teste seguinte mostrará um erro, porém é um erro esperado devido a formatação do ultimo print. Optamos por
    deixar assim para que o código fique mais visivel, para consertar o erro deveriamos colocar o print todo na
    mesma linha o que deixaria o código difícil de ser lido por outras pessoas.
    
    >>> info_usuario={"FATOR":'mínimo',"ALTURA":1.80,"IDADE":18,"NOME":"Gabriel","SEXO":'homem'}
    >>> MENSAGENS_ERROS(info_usuario)
    Olá, seja bem-vindo(a) ao nosso controle de dieta...Espero que sejamos bons amigos!)                 Peço que preencha sempre todos os dados sincera e adequadamente, e lembre-se,estou)                 aqui para ajudá-lo(a)... Observação: Este programa não substitui um acompanhamento)                 médico.)    1
    '''
    if info_usuario['FATOR'] not in ("mínimo","baixo","médio","alto","muito alto"):
        print('''Desculpe mas verificamos um erro no seu arquivo de entrada, parece que
                 seu fator de atividade física está em um padrão diferente, por favor 
                 corrija para que possamos continuar,isto será importante para realizarmos os calculos''')
        return 0
    # Reproduz uma mensagem de erro caso a altura do usuário não seja um numero decimal.
    if type(info_usuario['ALTURA']) != float:
        print('''Desculpe mas verificamos um erro no seu arquivo de entrada, parece que
                 sua altura está em um padrão diferente, por favor 
                 corrija para que possamos continuar,isto será importante para realizarmos os calculos''')
        return 0
    # Reproduz uma mensagem de erro caso a idade do usuario não seja um número inteiro.
    if type(info_usuario['IDADE']) !=int:
        print('''Desculpe mas verificamos um erro no seu arquivo de entrada, parece que
                 sua idade está em um padrão diferente, por favor 
                 corrija para que possamos continuar,isto será importante para realizarmos os calculos''')  
        return 0
    # Reproduz uma mensagem de erro caso o nome do usuário tenha menos que 2 caracteres.
    if len(info_usuario['NOME']) <= 1:
        print('''Desculpe mas verificamos um erro no seu arquivo de entrada, parece que
                 seu nome não é válido, por favor 
                 corrija para que possamos continuar''')  
        return 0
    # Reproduz uma mensagem de erro caso o sexo do usuário seja diferente de masculino ou feminino e homem ou mulher.
    if (info_usuario['SEXO']) not in ("homem","mulher","masculino","feminino"):
        print('''Desculpe mas verificamos um erro no seu arquivo de entrada, parece que
                 seu sexo está em um padrão diferente, por favor 
                 corrija para que possamos continuar,isto será importante para realizarmos os calculos''')
        return 0

      #Boas vindas  
    print('''Olá, seja bem-vindo(a) ao nosso controle de dieta...Espero que sejamos bons amigos!
             Peço que preencha sempre todos os dados sincera e adequadamente, e lembre-se,estou
             aqui para ajudá-lo(a)... Observação: Este programa não substitui um acompanhamento
             médico.''')
    return 1
