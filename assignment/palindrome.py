import sys
text=input("String : ")
l=len(text)
for i in range(l//2):
    if(text[i]!=text[l-i-1]):
        sys.exit("Not a Palindrome")
print("Palindrome")