# Autor: Thelsandro Antunes
# Data: 12/05/2017
# EST-UEA
# Disciplina: LP1
# Professora: Elloa B. Guedes
# 2 Lista de Exercicios (06/04/2015)
# Questao 34: Escreva um programa para gerar os cinquenta primeiros termos da 
#             serie: 1+n, 2*n, 3+n, 4*n, ... , onde n e um valor lido da unidade
#             padrao de entrada.
             

from __future__ import print_function

n=int(input("n?"))

print("50 primeiros termos da serie [1+n,2*n,3+n,4*n...]")
print()
for i in range(1,51):
  if((i%2)==0):
    print(i*n, end=", ")
  else:
    print(i+n, end=", ")  
