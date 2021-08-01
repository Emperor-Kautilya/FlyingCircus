#Name : Pranav Tiwari Rollno.201127
class Student:
    def __init__(self):
        self.rollno=input("Enter Rollno. :")
        self.name=input("Enter Name :")
        self.branch=input("Enter Branch :")
class Exam:
    def __init__(self,r):
        self.rollno=r
        self.marks1=int(input("Enter marks1 :"))
        self.marks2=int(input("Enter marks2 :"))
        self.marks3=int(input("Enter marks3 :"))
        self.marks4=int(input("Enter marks4 :"))
        self.marks5=int(input("Enter marks5 :"))
        self.marks6=int(input("Enter marks6 :"))

class Result(Student,Exam):
    def __init__(self):
        Student.__init__(self)
        Exam.__init__(self,self.rollno)
        self.totalmark=self.marks1+self.marks2+self.marks3+self.marks4+self.marks5+self.marks6
        self.result=self.totalmark/6
    def display(self):
        print("Total marks : ",self.totalmark)
        print("Result : ",self.result)
obj=Result()
obj.display()
