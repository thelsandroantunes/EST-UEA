# Autor: Thelsandro Antunes
# Data: 03/07/2017
# EST-UEA
# Disciplina: LP1
# Professora: Elloa B. Guedes
# 3 Lista de Exercicios (09/04/2015)
# Questao 19: Implemente uma funcao que retorne o somatorio dos quadrados dos n
#             primeiros numeros inteiros positivos. Ex: s = 1**2 + 2**2 + 3**2 + . . . + n**2

from __future__ import print_function

def somaN(n):
  
  s = 0
  for i in range(1,n+1,1):
    s = s + i**2
    
  return s
  
  
n = int(input("numero?"))

print("Ex: S(n) = 1**2 + 2**2 + 3**2 + . . . + n**2")
print()
print("    S(%d) "%n, end="=")
print(" %d"%somaN(n))


