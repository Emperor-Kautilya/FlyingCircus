text=input("Enter sentence : ")
sentence=text[0:-1]
words=sentence.split(" ")
words.sort(reverse=True,key=len)
print("Words\tLength")
for i in words:
    print(i,"\t",len(i))
