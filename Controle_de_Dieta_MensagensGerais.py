import numpy as np
import matplotlib.pyplot as plt


    # Reproduz uma mensagem de erro caso o fator de atividade fisica do usuário não seja um dos 5 indicados.
def MENSAGENS_ERROS(info_usuario):
    '''
    >>> info_usuario={"FATOR":'mínimo',"ALTURA":1.80,"IDADE":18,"NOME":"Gabriel","SEXO":'homem'}
    >>> MENSAGENS_ERROS(info_usuario)
    Olá, seja bem-vindo(a) ao nosso controle de dieta...Espero que sejamos bons amigos!\n                 Peço que preencha sempre todos os dados sincera e adequadamente, e lembre-se,estou\n                 aqui para ajudá-lo(a)... Observação: Este programa não substitui um acompanhamento\n                 médico.\n    1
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
    if (info_usuario['SEXO']) not in ("homem","mulher","masculino","feminino","M","H"):
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




def grafico_barras_acumuladas(calorias_recomendadas, calorias_semana, proteinas_semana, carboidratos_semana, gorduras_semana, dias):
#Cria uma variavel com a lista de dias
    ''' Testa se grafico_barras_acumuladas funciona adequadamente
        >>> grafico_barras_acumuladas(500,[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],4)
        [1, 2, 3, 4]
        '''
    contagem_dias = []
    
    for x in range(1,dias+1):
        contagem_dias.append(x)
    
    N = dias # Comprimento do eixo x=numero de dias
    hist1 = np.array([0] * N )
    hist2 = np.array([0] * N )
    hist3 = np.array([0] * N )
    hist4 = np.array([0] * N )
    hist5 = np.array([0] * N )
    
    #--- lista de cada coisa ingerida ---
    quantidades_calorias_recomendadas=[calorias_recomendadas]*dias
    
    #define o valor do eixo y. O valor para cada alimento será o valor dado na lista acima. 
    #Para x=1 pegara o item 0 da lista.
    for x in contagem_dias:
        hist1[x-1] =quantidades_calorias_recomendadas[x-1]
    for x in contagem_dias:
        hist2[x-1] +=calorias_semana[x-1]
    for x in contagem_dias:
        hist3[x-1] +=proteinas_semana[x-1]
    for x in contagem_dias:
        hist4[x-1] +=carboidratos_semana[x-1]
    for x in contagem_dias:
        hist5[x-1] +=gorduras_semana[x-1]
    teste1="Proteina(g)", "Carboidratos(g)", "Gordura(g)"
    teste2="Calorias sugeridas(Kcal)","Calorias ingeridas(Kcal)"
    #Setup dos gráficos de barras       
    
    
    plt.subplot(111)
    plt.bar( np.arange(0,N)+0.55, hist3, 0.3, color='#FFFF00')
    plt.bar( np.arange(0,N)+0.85, hist4, 0.3, color='#008000')
    plt.bar( np.arange(0,N)+1.15, hist5, 0.3, color='#3F62F5')
    
    #Legenda do gráfico    
    plt.legend(teste1,bbox_to_anchor=(1.0, -0.15),ncol=2,fancybox=True, shadow=True)
    plt.xlabel( 'Dias' )
    plt.ylabel( 'Quantidades' )
    #Limite dos eixos do gráfico
    plt.xticks( np.arange( 1,N+1 ) )
    plt.axis( [0.5, N+0.5, 0, max(hist3+hist4+hist5)] )
    plt.show()
    
    
    
    
    plt.subplot(111)
    plt.bar( np.arange(0,N)+0.55, hist1, 0.45, color='#FF0000')
    plt.bar( np.arange(0,N)+1, hist2, 0.45, color='#FF4500')
    
    #Legenda do gráfico  
    plt.legend(teste2,bbox_to_anchor=(1.0, -0.15),ncol=2,fancybox=True, shadow=True)
    plt.xlabel( 'Dias' )
    plt.ylabel( 'Quantidades' )
    #Limite dos eixos do gráfico
    plt.xticks( np.arange( 1,N+1 ) )
    plt.axis( [0.5, N+0.5, 0, max(5+ hist1+hist2)] )
    plt.show()
    
    return contagem_dias


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
normal='''Vale lembrar que mesmo assim recomenda-se uma nutricionista para acompanhar sua dieta.'''
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
    ('Vale lembrar que mesmo assim recomenda-se uma nutricionista para acompanhar sua dieta.', 'saudável')
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
    return REL_FINAL, RESULTADO

#----------------------------------------------------------------------------
