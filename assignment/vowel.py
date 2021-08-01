#Write a Python program to test whether a passed letter is a vowel or not.
ch=input("Enter a character : ")
s='aeiouAEIOU'
if ch in s:
    print('Vowel')
else:
    print('Not a Vowel')