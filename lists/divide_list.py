text=input("Original list: ")
n=int(input("Length of the first part of the list: "))
data=list(map(int,text.split(",")))
list2=data[n:]
list1=data[:n]
print(f"({list1},{list2})")
#print(list2)