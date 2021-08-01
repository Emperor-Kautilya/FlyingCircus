def EB_bill(): 
    unit=int(input("Enter the number of units : "))
    bill=250.0
    if unit<200:
        bill=bill+unit*3.0
    elif unit<500:
        bill=bill+(unit-200)*5.0+200*3.0
    elif unit<800:
     bill=bill+(unit-500)*7.0+300*5.0+200*3.0
    else:
      bill=bill+(unit-800)*10.0+300*7.0+300*5.0+200*3.0
    print("Bill without tax :",bill)
    bill=bill+0.170*bill
    print("Total Amount=",bill)
EB_bill()