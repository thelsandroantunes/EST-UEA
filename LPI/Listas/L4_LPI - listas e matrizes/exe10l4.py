# Autor: Thelsandro Antunes
# Data: 07/07/2017
# EST-UEA
# Disciplina: LP1
# Lista de Vetores e Matrizes
# Questao 10: Dada uma frase, envie-a para uma funcao e retorne-a em CamelCase.
#             
#             "CamelCase e a denominacao em ingles para a pratica de escrever palavras 
#             compostas ou frases, onde cada palavra e iniciada com Maiuscula e unidas sem           #             espacos."
#
#             Ex: "Minha casa, minha vida" -> "MinhaCasa,MinhaVida"
#
#             Dica: Para transformar as letras minusculas em maiusculas use a tabela ASCII e 
#             as funcoes ord() e chr().
#

from __future__ import print_function

def maiuscula(p):
  
  y = int(ord(p))-32  
  x = chr(y)
    
  return x

def CamelCase(lista):

  listaAux = []
  i = 1
  
  listaAux.append(maiuscula(lista[0]))
  
  while(i<len(lista)):
    if(lista[i] == " "):      
          
      listaAux.append(maiuscula(lista[i+1]))
      i = i + 1
    else:
      listaAux.append(lista[i])
    i = i + 1
   
  return listaAux


f = raw_input("Digite sua frase: ")

matx = CamelCase(f)

frase = ""
for i in matx:
  frase = frase + i

print(frase)
