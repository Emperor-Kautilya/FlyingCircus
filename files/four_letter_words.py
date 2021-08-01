fp=open("four_letter_word_file.txt",'r')
count=0
text=fp.read()
wordlist=text.split(" ")
for ch in wordlist:
    if(len(ch)==4):
        count+=1
print("Number of four letter word : ",count)