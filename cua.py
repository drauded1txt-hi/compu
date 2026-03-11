import random as r
c = []
k = []
for i in range(0,16):
  if i <=9:
    i = str(0)+str(i)
  i = str(i)
  c.append(i)
r.shuffle(c)
print(c)
print("",c[0:4],"\n",c[4:8],"\n",c[8:12],"\n",c[12:16])
for i in range(0,16):
  i = str(i)
  k.append(i)
print(k)
print(" Instrucciones:"+"\n"+"Eliga un numero y despues decida hacia donde moverlo")
print("Opciones de movimiento:","\n","Arriba = A","\n","Abajo = O","\n","Izquierda = I","\n","Derecha = D")
print("Para salir escriba S")
while c != k:
  mover = input("Que numero desea mover? ")
  if mover == "S":
    break
  for mover in range(0,16):
    if mover <=9:
      mover = str(0)+str(mover)
    mover = str(mover)
  if mover in c:
    idx = c.index(mover)
  else:
    print("El numero no esta en la lista")
  m = input("Hacia donde lo desea mover? ")
  if m == "I":
    c[idx-1] = mover
    
  print(c)
  print("",c[0:4],"\n",c[4:8],"\n",c[8:12],"\n",c[12:16])
