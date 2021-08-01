class Shape:
    def __init__(self,s):
        self.shape=s
    def area(self,r):
        print('area of',self.shape,":",str(3.14*r**2))
    def circumferece(self,r):
        print("circumferece of",self.shape,":",str(2*3.14*r),'\n')
    

class Rectangle(Shape):
    def __init__(self,l,b,s):
        self.length=l
        self.breadth=b
        Shape.__init__(self,s)
    def area(self):
        print('area of',self.shape,":",str(self.length*self.breadth))
    def circumferece(self):
        print("circumferece of",self.shape,":",str(2*(self.length+self.breadth)),'\n')        
    def getLength(self):
        return self.length
    def getBreadth (self):
        return self.breadth

class Circle (Shape):
    def __init__(self,r,s):
        Shape.__init__(self,s)
        self.radius=r
    def getRadius(self):
         return self.radius

obj2=Rectangle(10,5,"rectangle")
obj3=Circle(5,"Circle")
obj2.area()
obj2.circumferece()
length=obj2.getLength()
breadth=obj2.getBreadth()
obj3.area(obj3.radius)
obj3.circumferece(obj3.radius)
radius=obj3.getRadius()
print('length',length)
print('radius',radius)