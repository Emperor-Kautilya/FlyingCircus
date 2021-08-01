op=int(input("Enter :\n1->to check a number for prime\n2->to print prime no. in range (a,b)\n>>>"))
if op==1:
    n=int(input("Enter a number : "))
    for i in range(2,n//2+1):
        if(n%i==0):
            print("Not a prime number")
            exit()
    print("Prime number")
elif op==2:
    a=int(input("Enter a : "))
    b=int(input("Enter b : "))
    print("Prime numbers : ",end="")
    k=0
    for i in range(a+1,b):
        c=0
        for j in range(2,i//2+1):
            if(i%j==0):
                c=c+1
        if(c==0):
            print(i,end=" ")
            k=k+1
    print("")# to change line
    if(k==0):
        print("Not found")
else:
    print("Invalid Input")

        