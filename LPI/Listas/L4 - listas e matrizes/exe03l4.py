# Autor: Thelsandro Antunes
# Data: 06/07/2017
# EST-UEA
# Disciplina: LP1
# Lista de Vetores e Matrizes
# Questao 03: Escreva uma funcao em Python que receba uma lista de 10 (dez) numeros inteiros e
#             devolva quantos dos numeros sao primos.

from __future__ import print_function

def primo(n):
  
  Ehprimo = False
  resto = 0
  for i in range(1,n+1):
    if((n%i)==0):
      resto = resto + 1
  
  if(resto==2):
    Ehprimo = True
    
  return Ehprimo

lista = []

for i in range(6):
  print("%d "%(i+1), end="")
  aux = int(input("valor?"))
  lista.append(aux)

newLista = []  
for l in lista:  
  if primo(l):
    newLista.append(l)
    
print()
print("Numeros Primos")
print(newLista)
