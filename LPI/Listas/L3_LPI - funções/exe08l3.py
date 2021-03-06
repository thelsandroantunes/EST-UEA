# Autor: Thelsandro Antunes
# Data: 29/06/2017
# EST-UEA
# Disciplina: LP1
# Professora: Elloa B. Guedes
# 3 Lista de Exercicios (09/04/2015)
# Questao 08: Implemente um programa em Python que calcule a area de uma figura
#             geometrica. O programa deve possuir uma funcao para cada figura
#             geometrica e deve responde de forma satisfatoria a area do Circulo,
#             Triangulo, Quadrado, Trapezio e Retangulo.


def circulo(r,p):
  ac = p*r**2
  return ac


def triangulo(b,h):

  at = (b*h)/2
  return at

def quadrado(l):
  
  aq = l*l
  return aq


def trapezio(be,ba,h):
  
  atp = ((be + ba)*h)/2
  return atp

def retangulo(b,h):

  ar = b*h
  return ar


print("CIRCULO")
raio = float(input("Raio do circulo?"))
pi = 3.14

print("Area do circulo: %.2f" %(circulo(raio,pi)))
print("---------------------")

print("TRIANGULO")
base = float(input("Base do triangulo?"))
altura = float(input("Altura do triangulo?"))

print("Area do triangulo: %.2f" %(triangulo(base,altura)))
print("-----------------------")

print("QUADRADO")
lado = float(input("Lado do quadrado?"))

print("Area do quadrado: %.2f" %(quadrado(lado)))
print("----------------------")

print("TRAPEZIO")
baseMenor = float(input("Base Menor do trapezio?"))
baseMaior = float(input("Base Maior do trapezio?"))
altura = float(input("Altura do trapezio?"))

print("Area do trapezio: %.2f" %(trapezio(baseMenor, baseMaior, altura)))
print("----------------------")


print("RETANGULO")
base = float(input("Base do retangulo?"))
altura = float(input("Altura do retangulo?"))

print("Area do retangulo: %.2f" %(retangulo(base, altura)))
print("----------------------")
