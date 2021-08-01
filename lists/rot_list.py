text=input("Original list: ")
data=list(map(int,text.split(",")))
print(data)
n=int(input("Rotate By: "))
ch=int(input("Enter Choice:\n1.Rotate left\n2.Rotate right\n>>>: "))
if ch==1:
    print(data[n:]+data[:n])
else:
    n=n*-1
    print(data[n:]+data[:n])