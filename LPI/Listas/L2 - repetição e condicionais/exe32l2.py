# Autor: Thelsandro Antunes
# Data: 12/05/2017
# EST-UEA
# Disciplina: LP1
# Professora: Elloa B. Guedes
# 2 Lista de Exercicios (06/04/2015)
# Questao 32: Escreva um programa para determinar todos os numeros de 3 algarismos, 
#             cujas somas dos cubos dos algarismos sejam iguais ao proprio numero. 
#             Exemplo: 153 = 1**3 + 5**3 + 3**3 .

from __future__ import print_function

n=int(input("n?"))

a=n/100

b=(n%100)/10

c=(n%100)%10

soma_cubo = (a**3)+(b**3)+(c**3)

print("Soma dos cubos dos Algoritmos ")
print(a, end="^3 + ")
print(b,end="^3 + ")
print(c,end="^3 = ")
print(soma_cubo)

