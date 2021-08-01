text=input("Enter list : ")
data=list(map(int,text.split(",")))
n=len(data)
i=0
while i<n:
    ch=data[i]
    while(data.count(ch)>1):
        data.remove(ch)
    n=len(data)
    i=i+1
print(data)