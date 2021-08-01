#Write a Python Program to find fibonacci series upto N terms
n=int(input("Enter the number of terms in fibonnaci series : "))
f=0
s=1
print("Fibonnaci Series :")
if(n==1):
    print(f,' ')
elif(n==2):
    print(f,s)
else:
    print(f,s,end=' ')
    for i in range(2,n): 
        t=f+s
        print(t,end=' ')
        f=s
        s=t
print('\n')
    