# Autor: Thelsandro Antunes
# Data: 28/06/2017
# EST-UEA
# Disciplina: LP1
# Professora: Elloa B. Guedes
# 1 Lista de Exercicios (25/03/2015)
# Questao 15: Sabendo-se que o quilowatt de energia custa R$ 0.37, faca um programa
#             que receba a quantidade de quilowatts consumida por uma residencia
#             e imprima:
#             * O valor a ser pago por uma residencia;
#             * O valor a ser pago com desconto de 15%.

qw = float(input("quilowatt consumido?"))

print("--------------------------") 
print("valor de consumo = %.2f" %(qw*0.37) ) 
print("valor de desconto = %.2f" %((qw*0.85)*0.37)) 
