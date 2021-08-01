#function to calculate nth highest term in dictionary
def nth_max(dict,n):
    for key, value in dict.items():
        c=0
        for k, v in dict.items():
            #take difference of each number with all in list
            if value-v<=0:
                c+=1
        #if a number is nth highest it's difference with other terms
        #....will be negative only n times
        if(c==n):
            print (key,":",value,end="")
            return
    return

#empty dictionary
dict={}
while(True):
    k=input("Enter Key: ")
    v=float(input("Enter associated value: "))
    dict[k]=v
    #check if user want's to continue
    c=input("Would you like to continue ([y]/n)")
    if(c=="n"):
        break
dict={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
print("Top three elements are:")
nth_max(dict,1)
print(end=", ")
nth_max(dict,2)
print(end=", ")
nth_max(dict,3)