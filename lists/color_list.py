import sys
list1=input("Enter a colour list 1 :").split(", ")
list2=input("Enter a colour list 2 :").split(", ")
prev=0
print("Test common elements between color1 and color2 are in same order?")
for i in list1:#take out colours from one list
    if i in list2:#check if colour is in list 2
        if list2.index(i)>=prev:#colour should be present ahead of previous index
            prev=list2.index(i)#if so copy index to prev
        else:
            sys.exit("False")#if colur is not present ahead the they are not in order
print("True")
print("")