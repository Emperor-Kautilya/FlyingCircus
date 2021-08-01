class Vehicle:
    def __init__(self,name,mileage,capacity):
        self.name=name
        self.mileage=mileage
        self.capacity=capacity
    def fare(self):
        self.fare=self.capacity*100
        print('%-15s%-15s%-15s%-15s'%('name','mileage','capacity','fare'))
        print('%-15s%-15s%-15s%-15s'%(self.name,self.mileage,self.capacity,self.fare))
class Bus(Vehicle):
    def fare(self):
        self.fare=self.capacity*100
        self.fare=self.fare+(10/100)*self.fare
        print('%-15s%-15s%-15s%-15s'%('name','mileage','capacity','fare'))
        print('%-15s%-15s%-15s%-15s'%(self.name,self.mileage,self.capacity,self.fare))

name=input('enter name of vehicle : ') 
mileage=float(input('enter mileage of vehicle : '))
capacity=int(input('enter no. of seats : '))
if name.lower()=='bus':
    obj=Bus(name,mileage,capacity)
    obj.fare()
else:
    obj=Vehicle(name,mileage,capacity)
    obj.fare()