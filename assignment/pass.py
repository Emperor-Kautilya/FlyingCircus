import sys
password=input("Password : ")
l=len(password)
if l<6:
    sys.exit ("Password is not short ")
elif l>16:
    sys.exit ("Password is too long ")
flag1=True;flag2=True;flag3=True;flag4=True
for i in range(l):
    ch=password[i]
    if(ch.islower()):
        flag1=False
    elif(ch.isupper()):
        flag2=False
    elif(ch.isnumeric()):
        flag3=False
    elif(ch in "$#@"):
        flag4=False
    else:
        sys.exit("Invalid charater found : "+ch)
if(flag1):
    sys.exit ("Missing letter between [a-z]")  
if(flag2):
    sys.exit ("Missing letter between [A-Z]")    
if(flag3):
    sys.exit ("Missing number between [False-9]")
if(flag4):
    sys.exit ("Missing special character [$#@]")
print("Password Valid")