import math
a=int(input("Coeficient of x square : "))
b=int(input("Coeficient of x  : "))
c=int(input("Constant : "))
d=(b*b-4*a*c)
if d<0:
    print("Imaginary roots")
    d=-d
    print("Roots :\nx1=({}+({})i)/{}\tx2=({}-({})i)/{}".format(-b,math.sqrt(d),2*a,-b,math.sqrt(d),2*a))
elif d==0:
    print("Real and equal roots")
    print("Roots :\nx={},{}".format(-b/(2*a),-b/(2*a)))
else:
    print("Real and unique roots")
    print("Roots :\nx1={}\tx2={}".format((-b+math.sqrt(d))/(2*a),(-b-math.sqrt(d))/(2*a)))