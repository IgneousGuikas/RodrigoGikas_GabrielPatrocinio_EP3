import numpy as np
import matplotlib.pyplot as plt
def grafico_barras_acumuladas(calorias_diarias, calorias_semana, proteinas_semana, carboidratos_semana, gorduras_semana, dias):
#Cria uma variavel com a lista de dias
    ''' Testa se grafico_barras_acumuladas funciona adequadamente
        >>> grafico_barras_acumuladas(500,[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],4)
        [1, 2, 3, 4]
        '''
    contagem_dias=[]
    
    for x in range(1,dias+1):
        contagem_dias.append(x)
    
    samples1 = contagem_dias
    
    N = dias # Comprimento do eixo x=numero de dias
    hist1 = np.array([0] * N )
    hist2 = np.array([0] * N )
    hist3 = np.array([0] * N )
    hist4 = np.array([0] * N )
    hist5 = np.array([0] * N )
    
    #--- lista de cada coisa ingerida ---
    quantidades_calorias_diarias=[calorias_diarias]*dias
    
    #define o valor do eixo y. O valor para cada alimento será o valor dado na lista acima. 
    #Para x=1 pegara o item 0 da lista.
    for x in samples1:
        hist1[x-1] =quantidades_calorias_diarias[x-1]
    for x in samples1:
        hist2[x-1] +=calorias_semana[x-1]
    for x in samples1:
        hist3[x-1] +=proteinas_semana[x-1]
    for x in samples1:
        hist4[x-1] +=carboidratos_semana[x-1]
    for x in samples1:
        hist5[x-1] +=gorduras_semana[x-1]
    teste="Calorias sugeridas(Kcal)","Calorias ingeridas(Kcal)","Proteina(g)", "Carboidratos(g)", "Gordura(g)"
    #Setup do gráfico de barras       
    width = 1
    plt.bar( np.arange(0,N)+0.5, hist1, width, color='#FF0000' )
    plt.bar( np.arange(0,N)+0.5, hist2, width, color='#FF4500', bottom=hist1 )
    plt.bar( np.arange(0,N)+0.5, hist3, width, color='#FFFF00', bottom=hist1+hist2 )
    plt.bar( np.arange(0,N)+0.5, hist4, width, color='#008000', bottom=hist1+hist2+hist3 )
    plt.bar( np.arange(0,N)+0.5, hist4, width, color='#3F62F5', bottom=hist1+hist2+hist3+hist4 )
    #Legenda do gráfico
    plt.legend(teste,bbox_to_anchor=(1.0, -0.15),ncol=2,fancybox=True, shadow=True)
    plt.xlabel( 'Dia' )
    plt.ylabel( 'Quantidades ingeridas' )
    #Limite dos eixos do gráfico
    plt.xticks( np.arange( 1,N+1 ) )
    plt.axis( [width/2.0, N+width/2.0, 0, max(5+ hist1+hist2+hist3+hist4+hist5)] )
    plt.show()
    return contagem_dias
gráfico_barras_acumuladas()