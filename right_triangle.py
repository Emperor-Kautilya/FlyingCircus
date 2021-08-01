a=int(input("Length of Side 1 : "))
b=int(input("Length of Side 2 : "))
c=int(input("Length of Side 3 : "))
if(a>b and a>c):
    if(a*a==b*b+c*c):
     print("Right angle triangle")
     exit()
elif(b>a and b>c):
    if(b*b==a*a+c*c):
     print("Right angle triangle")
     exit()
else:
    if(c*c==b*b+a*a):
     print("Right angle triangle")
     exit()
print("Not a right angle triangle")
