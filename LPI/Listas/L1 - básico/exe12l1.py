# Autor: Thelsandro Antunes
# Data: 28/06/2017
# EST-UEA
# Disciplina: LP1
# Professora: Elloa B. Guedes
# 1 Lista de Exercicios (25/03/2015)
# Questao 12: Faca um programa que leia um numero real qualquer e apresente na
#             saida: a parte inteira deste numero; a parte fracionaria e o arredonda-
#             mento deste numero.

n=float(input("numero?"))

print("parte inteira: %d" %n)
print("parte fracionaria: %.2f" %(n-int(n)))
print("parte arrendondamento: %.1f" %(round(n)))

