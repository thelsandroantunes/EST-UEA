# Autor: Thelsandro Antunes
# Data: 12/07/2017
# EST-UEA
# Disciplina: LP1
# Lista de Vetores e Matrizes
# Questao 15: Faca um programa que leia duas matrizes, envie as matrizes para uma funcao que
#             verifica se as mesmas podem ser multiplicadas. Caso positivo, envie as matrizes para
#             uma outra funcao que efetuara a multiplicacao entre as matrizes e retornara uma terceira
#             matriz, caso negativo, escreva na tela uma mensagem.

from __future__ import print_function
from random import randint


def prodMatrix(A,B):

  vet = []  

  linA = len(A)
  colA = len(A[0])
  colB = len(B[0])

  for i in range(linA):    
    vet.append([])
    for j in range(colB): 
      mult = 0
      for k in range(colA):              
        mult = mult + (A[i][k] * B[k][j])      
      vet[i].append(mult)
      
  return vet
  
  

def multIf(colA,linB):
  
  ok = False
  if(colA==linB):
    ok = True
    
  return ok
 
def le(lin,col):
  
  vet = []  
  for i in range(lin):
    lista = []
    for j in range(col):    
      #aux = randint(1,100)
      aux = int(input())
      lista.append(aux)
    vet.append(lista)
  return vet

def imprime(vet, lin, col):

  for i in range(lin):
    print("")
    for j in range(col):
      print("[%d] "%vet[i][j], end=" ")
    

    

A = []
Alin = int(input("Ai?"))
Acol = int(input("Aj?"))

B = []
Blin = int(input("Bi?"))
Bcol = int(input("Bj?"))

A = le(Alin,Acol)
B = le(Blin,Bcol)

print("\n\nMatriz A")
imprime(A,Alin,Acol)
print("\n\nMatriz B")
imprime(B,Blin,Bcol)

if not multIf(Acol,Blin):
  print("\n\nNao pode efetuar a multiplicao das matrizes [AXB]")
else:
  matx = prodMatrix(A,B)
  print("\n\nNOVA Matriz")
  imprime(matx, len(matx), len(matx[0]))
  


