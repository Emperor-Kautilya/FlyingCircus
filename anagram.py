import sys
def DecimalToBinary(num):
    res=""
    if num==1:
        return "1"
    return str(num%2)+DecimalToBinary(num // 2)
a=int(input("Enter a :"))
b=int(input("Enter b :"))
list1=list(DecimalToBinary(a))
list2=list(DecimalToBinary(b))
n=max(len(list1),len(list2))
if(list1.count('1')==list2.count('1')):
    if(n-list1.count('1')==n-list2.count('1')):
        sys.exit("Anagram")
print("Not an anagram")
