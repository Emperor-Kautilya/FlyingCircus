#enter data
text=input("Enter data : ")
#identify whether input data is string or list
if text[0]=="[":
    data=list(text[1:len(text)-1].split(", "))#removce block if list is given within blocks
else:
    data=list(text[1:len(text)-1].split(", "))#remove inverted comma's if list is given within inverted commas
#counter to traverse through [1, 1, 2, 3, 4, 4.3, 5, 1] the data
i=0
print(data)
#print starting block
print("List reflecting the run-length encoding from the said data:\n[",end="")
while i<len(data):
    ch=data[i]
    c=1
    #check if next character is same if there exist one
    while(i<len(data)-1 and data[i+1]==ch):
            c+=1#increase counter
            i+=1#move ahead 
    #print count followed by comma for middle element else only count
    print(f"[{c},'{ch}']",end=",") if i<len(data)-1 else print(f"[{c},'{ch}']",end="]\n")
    i+=1
