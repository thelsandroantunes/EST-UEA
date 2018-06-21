# Autor: Thelsandro Antunes
# Data: 10/07/2017
# EST-UEA
# Disciplina: LP1
# Lista de Vetores e Matrizes
# Questao 11: Faca uma funcao em Python que leia um numero inteiro e retorne um vetor contendo
#             todos os divisores exatos deste numero. Considere que serao fornecidos apenas numeros
#             positivos como entrada.

def divisorEx(x,y):
  
  r = False
  if(x%y == 0):
    r = True
  
  return r


def numVetor(n):

  lista = []
  for i in range(n,0,-1):

    if divisorEx(n,i):
      lista.append(i)
  return lista


num = int(input("numero?"))
while(num<0):
  num = int(input("numero?"))

matx = numVetor(num)
print(matx)


