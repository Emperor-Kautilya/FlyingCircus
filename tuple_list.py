test_list = [(6, 5, 8),(6, 5, 8),(2, 7), (9, ),(2, 7)]
new_list=[]
for item in test_list:
    c=1
    while(test_list.count(item)>1):
        test_list.reverse()
        test_list.remove(item)
        test_list.reverse()
        c+=1
    l=(*item,c)
    new_list.append(l)
print(new_list)
