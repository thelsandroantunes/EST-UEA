# Autor: Thelsandro Antunes
# Data: 13/05/2017
# EST-UEA
# Disciplina: LP1
# Professora: Elloa B. Guedes
# 2 Lista de Exercicios (06/04/2015)
# Questao 54: (UEA/EST 2014.1) Faca um algoritmo para ler 100 numeros inteiros e
#             positivos. Na leitura dos numeros, o usuario pode informar numeros ne-
#             gativos, os quais nao devem ser considerados. Dentre os numeros lidos,
#             identifique o maior deles e imprima-o. Em seguida, algumas caracte-
#             risticas adicionais do maior numero devem ser informadas ao usuario:
#             quantos divisores exatos ele possui (excetuando-se o proprio numero) e
#             se ele e abundante, defectivo ou perfeito. Utilize as informacoes a seguir
#             para lhe auxiliar na resolucao da questao. Veja tambem um exemplo
#             de execucao.
#
#             * Um numero e dito ser abundante quando a soma dos seus divisores
#               exatos, excetuando-se o proprio numero, e maior que o proprio
#               numero. Ex.: 12 < 1 + 2 + 3 + 4 + 6;
#             * Um numero e dito ser perfeito quando a soma dos seus diviso-
#               res exatos, excetuando-se o proprio numero, e igual ao proprio
#               numero. Ex.: 28 = 1 + 2 + 4 + 7 + 14;
#             * Um numero e dito ser defectivo quando a soma dos seus divisores
#               exatos, excetuando-se o proprio numero, e menor que o proprio
#               numero. Ex.: 15 < 1 + 3 + 5.
#


from __future__ import print_function

def divex(n):
  soma=0
  print("Divisores exatos: ")
  for i in range(1,n):
    if((n%i)==0):
      soma = soma + i
      print(i,end=",")  
  
  if(soma > n):
    print("")
    print("Numero Abundante")
  elif(soma == n):
    print("")
    print("Numero Perfeito")
  else:
    print("")
    print("Numero Defectivo")        

maior=0
for i in range(3):
  x=int(input("n?"))
  while(x<=0):
    x=int(input("n?"))
  if(maior<x):
    maior=x
    
print("Maior Numero: ", maior)
divex(maior)   
    





