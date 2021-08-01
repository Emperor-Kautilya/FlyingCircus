#Write a program to calculate the compound interest for the given inputs.
#Enter principle amount in pa variable
pa=float(input("Enter Principle Amount= "))
#Enter Rate of Interest per annum in percentage in rate variable
rate=float(input("Enter Rate of Interest in %age per annum= "))
#Enter time in years in time variable
time=float(input("Enter Time (in years)= "))
#Calculate final amount
fa=pa*((1+rate/100)**time)
#Calculate Compound Interest = Final Amount - Initial Amount
CI=fa-pa
print("Compound Interest= ",CI)
print("Final Amount= ",fa)