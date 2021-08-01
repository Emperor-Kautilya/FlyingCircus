#enter array
text=input("Enter array : ")
t=int(input("Enter target : "))
array=list(map(int,(text[1:len(text)-1].split(","))))#removce block if list is given within blocks
array1=array
c=1
for i in array:
    if(array.count(i)>1):
        array.remove(i)
        c+=1
    j=t-i
    if j in array:
        print("{},{}".format(array1.index(i)+c,array1.index(j)+c))
        array.remove(j)
    i=i+1
