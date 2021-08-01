text=input("Enter list : ")
data=list(map(int,text.split(",")))
for ch in data:
    while(data.count(ch)>1):
        data.remove(ch)
print(data)
