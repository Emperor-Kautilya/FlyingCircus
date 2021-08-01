l=[]
inp=input("Enter a list :")
val=inp.split()
i=0
for i in range(len(val)):
    l.append(val[i])
    if i>0:
        if val[i]==val[i-1]:
            l.reverse()
            l.remove(val[i])
            l.reverse()
print(l)