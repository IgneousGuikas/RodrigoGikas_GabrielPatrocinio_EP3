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


