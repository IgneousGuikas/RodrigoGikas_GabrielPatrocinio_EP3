from Controle_de_Dieta_Calculos import *
from Controle_de_Dieta_Dados import *
from Controle_de_Dieta_MensagensGerais import *

# puxa o catálogo de alimentos do arquivo alimentos.csv
fin = open('alimentos.csv', 'r', encoding='utf-8')

fin.readline()
middle = fin.readlines()
fin.close()

lista_alimentos= []
for termo in middle: # adiciona a lista_alimentos linhas do arquivo alimentos.csv como termos
    lista_alimentos.append(termo.strip())


# puxa as informações do usuário do arquivo usuario.csv
fin = open('usuario.csv', 'r', encoding='utf-8')

lista_usuario = []

fin.readline()
middle = fin.readline()
lista_usuario.append(middle.strip()) # adiciona a lista_usuario a linha do arquivo usuario.csv com as informações do usuario

fin.readline()
middle = fin.readlines() # adiciona a lista_usuario linhas do arquivo usuario.csv com os alimentos e suas quantidades ingeridas
fin.close()

for termo in middle:
    lista_usuario.append(termo.strip())



erros = 1 # variável que indica a existência de erros de parâmetros nas informações do usuário

while True:    
    catalogo = processa_dados_alimentos(lista_alimentos)
    info_usuario,consumo_semana = processa_dados_usuario(lista_usuario)
    
    # se houver erro nas informações do usuário, mostra uma mensagem de erro e fecha o programa, caso contrário mostra uma mensagem de boas vindas
    erros = MENSAGENS_ERROS(info_usuario)
    
    lista_dias, erros, calorias_semana, proteinas_semana, carboidratos_semana, gorduras_semana = pesquisa_alimentos(catalogo, consumo_semana)
    
    if erros == 0:
        break
    else:
        None
    
    calorias_recomendadas = calcula_calorias_recomendadas(info_usuario)
    IMC = calcula_IMC(info_usuario)
    dias, total = total_calorias_ingeridas(calorias_semana)
    
    grafico_barras_acumuladas(calorias_recomendadas, calorias_semana, proteinas_semana, carboidratos_semana, gorduras_semana, dias, lista_dias)    
    
    
    REL_FINAL, RESULTADO = FAIXA_IMC(IMC)
    COMPARACAO, MEDIA_CAL = CALCULA_COMPARACAO(total, calorias_recomendadas, dias)
    DIFERENCA, quantidade = ganho_ou_perda_massa(total, calorias_recomendadas)
    
    
    
    #Cria um arquivo txt chamado "Relatório Final" com as especificações do usuário: 
    relatorio_final=open("Relatório Final.txt","w",encoding="utf-8")
    relatorio_final.writelines('''De acordo com sua dieta e seus dados, calculei que seu IMC é %3.2f,
    isto indica que você está %s. Percebi também que você está
    ingerindo, em média %3.2f calorias %s recomendado,o que resultou %s de %3.2f gramas.\n\n\n%s''' % (IMC,RESULTADO,MEDIA_CAL,COMPARACAO,DIFERENCA,quantidade,REL_FINAL))
    relatorio_final.close()
    break
