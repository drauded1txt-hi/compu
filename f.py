import sys as s
x=int(s.argv[1])-2
c=[0,1]
for i in range(0,x):
    z=int(c[i]+c[i+1])
    c.append(z)
print(c)
