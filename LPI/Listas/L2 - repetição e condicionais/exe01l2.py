# Autor: Thelsandro Antunes
# Data: 31/03/2017
# EST-UEA
# Disciplina: LP1
# Professora: Elloa B. Guedes
# 2 Lista de Exercicios (06/04/2015)
# Questao 01: Escreva um programa para ler tres numeros reais quaisquer e imprimir
#             estes numeros em ordem numerica crescente.

a = float(input())
b = float(input())
c = float(input())

if(a>b and a>c):
  if(b>c):
    print(c,b,a)
  else:
    print(b,c,a)
else:
  if(b>a and b>c):
    if(a>c):
      print(c,a,b)
    else:
      print(a,c,b)
  else:
    if(c>a and c>b):
      if(a>b):
        print(b,a,c)
      else:
        print(a,b,c)
