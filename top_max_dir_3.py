#empty dictionary
dict={}
while(True):
    k=input("Enter Key : ")
    v=float(input("Enter associated value : "))
    dict[k]=v
    #check if user want's to continue
    c=input("Would you like to continue ([y]/n) : ")
    if(c=="n"):
        break
#dict={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
#store the dictionary in a list
value_list=list(dict.items())
#sort the list on basis of values
value_list.sort(key=lambda x:x[1],reverse=True)
print("Top three elements are:")
print(value_list[0],end=", ")
print(value_list[1],end=", ")
print(value_list[2])