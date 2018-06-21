# Autor: Thelsandro Antunes
# Data: 13/05/2017
# EST-UEA
# Disciplina: LP1
# Professora: Elloa B. Guedes
# 2 Lista de Exercicios (06/04/2015)
# Questao 50: Escreva um programa que receba como entrada dois numeros inteiros
#             n e p e que calcule o numero de combinacoes de n tomado de p a p de
#             acordo com a seguinte formula:
#
#             C[n,p] = n! / (p!(n − p)!)


from __future__ import print_function

def fatorial(n):
  fat=1

  for i in range(n,1,-1):
    fat=fat*i
  
  return fat

n=int(input("n?"))
p=int(input("p?"))

C = fatorial(n)/fatorial(p)*fatorial(n-p)

print("Numero de combinacoes: ", C)
