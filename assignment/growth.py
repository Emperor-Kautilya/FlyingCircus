import math
initial=int(input("Initial number of organisms : "))
rate=float(input("Rate  of growth : "))
n=float(input("Growth period to achieve this rate(in hrs) : "))
t=float(input("Time for population to grow : "))
final=initial*rate**(t/n)
#number of organisms cannot be in fraction
print("Final number of organism",math.floor(final))