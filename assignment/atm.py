w=float(input("Enter the withdrawal amount : "))
amt=float(input("Enter the initial balance : "))
if w%5==0:
    #amt should be a multiple of 5
    if (w+0.50)<amt:
        #amt should be able to cover the transition charges too
        amt=amt-w-0.50
print(amt)
