# Autor: Thelsandro Antunes
# Data: 29/06/2017
# EST-UEA
# Disciplina: LP1
# Professora: Elloa B. Guedes
# 3 Lista de Exercicios (09/04/2015)
# Questao 07: Implemente uma funcao em Python que retorne o quadrado de um
#             numero lido do teclado.

from __future__ import print_function

def quadrado(num):
  
  q = num**2

  return q


n = int(input("numero?"))

print("Quadrado: %d" %(quadrado(n)))

