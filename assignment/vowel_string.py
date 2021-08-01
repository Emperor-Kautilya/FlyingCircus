import sys
str=input("Enter String : ")
flag=0
for i in range(0,len(str)):
    ch=str[i]
    if ch in "aeiouAEIOU":
        flag=1
if flag==0:
    print("Wrong Input")
else:
    print("Valid String")