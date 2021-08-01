import csv
name=input("Enter the record file name : ")
file=open(name,'r')
text=csv.reader(file)
print("%-20s%-15s%-15s"%("Employee's name","The hours worked","Wages paid"))
for line in text:
    wordlist=line
    lname=wordlist[0]
    W_hrs=int(wordlist[1])
    h_wages=int(wordlist[2])
    price=W_hrs*h_wages
    print("%-20s%-15d%-15.2f"%(lname,W_hrs,price))
        