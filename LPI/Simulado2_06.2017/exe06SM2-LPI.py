
matx=[]

def bolha(lista):
  fim=len(lista)
  siga = True
  
  while((fim>1) and (siga)):
    trocou = False
    x=0
    
    while(x<fim-1):
      if(lista[x] > lista[x+1]):
        trocou = True
        aux = lista[x]
        lista[x] = lista[x+1]
        lista[x+1] = aux
      x = x + 1
      
    if not trocou :
      siga = False
    fim = fim - 1
    
    return lista

i=0
while(i<7):
  aux = int(input("num? "))
  
  if aux < 0:
    i = i - 1
  else:
    matx.append(aux)    
  i = i + 1
  
somaDiv=[]
tam = len(matx)
for i in range(tam):
  n = matx[i]
  soma=0
  for j in range(1,n+1):
    if(n%j==0):
      soma = soma + j
  somaDiv.append(soma)

print("Listas")  
print(matx)  
print(" ")
print(somaDiv)
print(" ")
print("Listas Ordenadas")  
bolha(matx)
bolha(somaDiv)

print(matx)  
print(" ")
print(somaDiv)
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
