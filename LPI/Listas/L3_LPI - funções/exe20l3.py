# Autor: Thelsandro Antunes
# Data: 03/07/2017
# EST-UEA
# Disciplina: LP1
# Professora: Elloa B. Guedes
# 3 Lista de Exercicios (09/04/2015)
# Questao 20: Implemente uma funcao em Python que verifique se um numero e primo.

def primo(n):
  
  Ehprimo = False
  resto = 0
  for i in range(1,n+1):
    if((n%i)==0):
      resto = resto + 1
  
  if(resto==2):
    Ehprimo = True
    
  return Ehprimo
  
  
n = int(input("numero?"))

if primo(n) :
  print("E primo")
else:
  print("NAO e primo")

