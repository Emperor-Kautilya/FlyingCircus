a=int(input("Enter first number : "))
b=int(input("Enter second number : "))
print("Gcd of",a,"and",b,"is",end=" ")
while a!=b:
    if a>b:
        a=a-b
    elif b>a:
        b=b-a
print(a)
