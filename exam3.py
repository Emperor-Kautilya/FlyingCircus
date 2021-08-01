print("enter coordinates of centre :")
cx=float(input("x="))
cy=float(input("y="))
r=float(input("radius="))
print("enter coordinates of point :")
px=float(input("x="))
py=float(input("y="))
d=(px-cx)**2+(py-cy)**2
if d==r*r:
    print("Point lies on the circle")
elif d>r*r:
    print("Point outside of the circle")
else:
    print("Point inside of the circle")