import random as r
c = []
for i in range(0,16):
  if i <=9:
    i = str(0)+str(i)
  i = str(i)
  c.append(i)
  r.shuffle(c)
print(c)
print("",c[0:4],"\n",c[4:8],"\n",c[8:12],"\n",c[12:16])

