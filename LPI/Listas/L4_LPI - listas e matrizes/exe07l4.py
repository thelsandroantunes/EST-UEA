# Data: 06/07/2017
# EST-UEA
# Disciplina: LP1
# Lista de Vetores e Matrizes
# Questao 07: Crie uma funcao que verifique se duas listas, dadas com parametro, sao iguais.

from __future__ import print_function

def igualdade(x,y):
  
  
  for i in range(len(x)):
    if(x[i] == y[i]):
      r = True
    else:
      r = False

  return r
  
  
lista1 = []

print("LISTA 1 ")
for i in range(3):
  print("%d "%(i+1), end="")
  aux = int(input("valor?"))
  lista1.append(aux)
  
lista2 = []
print("LISTA 2 ")
for i in range(3):
  print("%d "%(i+1), end="")
  aux = int(input("valor?"))
  lista2.append(aux)
  
  
print(igualdade(lista1,lista2))
