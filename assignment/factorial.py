# Write a Python Program for factorial of a number
num=int(input("Enter a number : "))
result=1
if(num<0):
    print("Factorial of negative number does not exist")
else:
    for i in range(1,num+1):
        result=result*i
    print("Factorial of {} is {}".format(num,result))
