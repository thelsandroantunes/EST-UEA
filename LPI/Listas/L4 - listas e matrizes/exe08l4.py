# Autor: Thelsandro Antunes
# Data: 07/07/2017
# EST-UEA
# Disciplina: LP1
# Lista de Vetores e Matrizes
# Questao 08: Escreva uma funcao em Python que receba uma lista com 20 valores inteiros,
#             informados pelo usuario e apresente o maior, o menor e suas respectivas posicoes em
#             que os mesmos foram informados. Caso existam numeros iguais mostre a posicao da
#             primeira ocorrencia.


from __future__ import print_function

def mamepo(l):
  
  maior = l[0]
  posMaior = 0
  menor = l[0]
  posMenor = 0
  for x in range(len(l)):
    if(maior < l[x]):
      maior = l[x]
      posMaior = x
    if(menor > l[x]):
      menor = l[x]
      posMenor = x

  print()
  print("Maior: %d - "%maior, end="")
  print("pos: [%d]"%posMaior)
  print("Maior: %d - "%menor, end="")
  print("pos: [%d]"%posMenor)

lista = []

print("LISTA 1 ")
for i in range(20):
  print("%d "%(i+1), end="")
  aux = int(input("valor?"))
  lista.append(aux)
  
mamepo(lista)
  
