n=int(input("Number : "))
m=n
sum=0
while m!=0:
    d=m%10
    sum+=d*d*d
    m=m//10
if sum==n:
    print("Armstrong number")
else:
    print("Not a Armstrong number")