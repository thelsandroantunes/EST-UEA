# Autor: Thelsandro Antunes
# Data: 06/07/2017
# EST-UEA
# Disciplina: LP1
# Lista de Vetores e Matrizes
# Questao 05: Escreva uma funcao que retorne uma matriz contendo 
#             a tabela verdade das funcoes and e or.

from __future__ import print_function

def tabela(p,q):
  
  matx = []
  
  for i in range(4):
    lista = []
    if(i<2):
      lista.append(p)
    else:
      p = False
      lista.append(p)  
      
    if(i%2!=0):
      q = False
      lista.append(q)
    else:
      q = True
      lista.append(q)
    
    a = (p and q)
    lista.append(a)
    b = (p or q)
    lista.append(b)
    
    matx.append(lista)
  
  return matx
  

p = True
q = True

l = tabela(p,q)

print()
print(" P         Q     P and Q   P or Q")
for i in range(4):
  print()
  for j in range(4):
    if(i<2):
      print(l[i][j], end="     ")
    else:
      print(l[i][j], end="    ")


