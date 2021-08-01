T=int(input())
for i in range(T):
    N,x,k=input().split()
    N=int(N)
    x=int(x)
    k=int(k)
    flag=0
    for j in range(0,(N+2),k):
        if j==x or x==N+1-j:
            print("YES")
            flag=1
    if flag==0:
        print("NO")