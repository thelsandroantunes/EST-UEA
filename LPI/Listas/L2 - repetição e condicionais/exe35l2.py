# Autor: Thelsandro Antunes
# Data: 12/05/2017
# EST-UEA
# Disciplina: LP1
# Professora: Elloa B. Guedes
# 2 Lista de Exercicios (06/04/2015)
# Questao 35: Faca um algoritmo que ajude uma crianca a aprender multiplicacao,
#             criando uma tabela para cada digito ( 0 - 9 ). Por exemplo, para o 9
#             tem-se:
#             9 x 0 = 0
#             9 x 1 = 9
#             9 x 2 = 18
#             ...
#             9 x 10 = 90


from __future__ import print_function

for i in range(1,10):
  print("**************")  
  for j in range(11):
    print("*",i,end=" X ")
    print(j,end=" =")
    print(i*j,"  *")
  print("**************")  
