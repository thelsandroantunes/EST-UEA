# Autor: Thelsandro Antunes
# Data: 04/07/2017
# EST-UEA
# Disciplina: LP1
# Professora: Elloa B. Guedes
# 3 Lista de Exercicios (09/04/2015)
# Questao 26: Escreva uma funcao que recebe um inteiro positivo m e devolve verdadeiro
#             se m e primo e 0 em caso contrario.


def primo(n):
  
  Ehprimo = False
  resto = 0
  for i in range(1,n+1):
    if((n%i)==0):
      resto = resto + 1
  
  if(resto==2):
    Ehprimo = True
    
  return Ehprimo
  
  
def positivo(m):
  if primo(m):
    return "verdadeiro"
  else:
    return "0"
  
m = int(input("m?"))

while(m<0):
  m = int(input("m?"))

print()

print("%s" %positivo(m))
