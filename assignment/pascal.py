import math
n=int(input("Enter number of lines : "))
for i in range(n,0,-1):
    for j in range(0,i):
        print(end="  ")
        n1=n-i
    for r in range(0,n1+1):
        c=math.factorial(n1)/(math.factorial(r)*math.factorial(n1-r))
        print("%4d" %int(c),end="")
    print()
    