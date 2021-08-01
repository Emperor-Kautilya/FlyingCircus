text=input("Enter Text : ")
max_freq=0;max=''
for i in range(len(text)):
    count=0
    for j in range(i,len(text)):
        if(text[i]==text[j]):
            count+=1
    if(count>max_freq):
        max_freq=count
        max=text[i]
print(f"Character with maximum frequency : '{max}'")