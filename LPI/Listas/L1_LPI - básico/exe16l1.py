# Autor: Thelsandro Antunes
# Data: 28/06/2017
# EST-UEA
# Disciplina: LP1
# Professora: Elloa B. Guedes
# 1 Lista de Exercicios (25/03/2015)
# Questao 15: Faca um programa que leia da entrada padrao o tamanho de um arquivo
#             para download (em MB) e a velocidade de um link de internet (em
#             Mbps), calcule e informe o tempo aproximado de download do arquivo
#             usando este link (em minutos).

tam = float(input("tamanho(MB)?"))
vel = float(input("velocidade(Mbps)"))

b=tam*8

print("tempo de download: %.2f" %((b-vel)/60))
