fib_list=[]
def Fibonacci(n):
    f=0
    s=1
    if(n==1):
        fib_list.append(f)
    elif(n==2):
        fib_list.append(f)
        fib_list.append(s)
    elif(n>2):
        fib_list.append(f)
        fib_list.append(s)
        for i in range(2,n):
            t=f+s
            fib_list.append(t)
            f=s
            s=t
def find_index():
    key=int(input("Enter element to search: "))
    if(key in fib_list):
        return(fib_list.index(key)+1)
    else:
        return 0
n=int(input("Enter the number of terms: "))
Fibonacci(n)
print("Fibonacci series : ",fib_list)
index=find_index()
if(index==0):
    print("Element no present")
else:
    print("Element present at position : ",index)