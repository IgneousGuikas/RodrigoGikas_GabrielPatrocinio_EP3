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
