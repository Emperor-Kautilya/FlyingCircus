import sys
text=input("Parentheses Expression : ")
stack=list()
p=list("{([])}")
for i in text:
    if(i in p):
        if(len(stack)==0 or p.index(i)<3):
            stack.append(i)
        elif (p.index(stack[-1])== 5-p.index(i)):
            stack.pop()
        else:
            sys.exit("Invalid expression!!")
if(len(stack)==0):
    print("Valid Epression!!")
else:
    print("Invalid Expression!!")