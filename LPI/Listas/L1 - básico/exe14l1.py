# Autor: Thelsandro Antunes
# Data: 28/06/2017
# EST-UEA
# Disciplina: LP1
# Professora: Elloa B. Guedes
# 1 Lista de Exercicios (25/03/2015)
# Questao 14: Faca um programa que leia uma string e imprima na saida padrao
#             apenas os caracteres definidos pelos indices fornecidos pelo usuario.

pal = str(raw_input("string?"))
i = int(input("inicio da string?")) 
f = int(input("fim da string?")) 

print(pal[i:f+1])
