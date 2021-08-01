matrix=input("Input Matrix : ")
r=int(input("R="))
c=int(input("C="))
data1=matrix[2:-2].split("}, {")
print("Output : ")
a=""
for i in data1:
    rows=i.split(", ")
    for j in rows:
        for k in range(c):
            a=a+j+" "
for i in range(r):
    print(a)