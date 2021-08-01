# function to return key for any value
def get_key(my_dict,val):
    for key, value in my_dict.items():
         if val == value:
             return key
    return "key doesn't exist"
#empty dictionary
dict={}
while(True):
    k=input("Enter Key: ")
    v=float(input("Enter associated value: "))
    dict[k]=v
    #check if user want's to continue
    c=input("Would you like to continue ([y]/n): ")
    if(c=="n"):
        break
dict={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
#store dictionary values in a list
value_list=list(dict.values())
#sort the list in ascending order
value_list.sort()
#reverse the list
value_list.reverse()
#display all top three values with there keys
print("Top three elements are:")
print(get_key(dict,value_list[0]),":",value_list[0],end=", ")
print(get_key(dict,value_list[1]),":",value_list[1],end=", ")
print(get_key(dict,value_list[2]),":",value_list[2])