#Write a program to find the sum of squares of odd no.s and even no.s upto 'n'
n=int(input("Enter n : "))
#a tells us the number of even terms upto n 
a=n//2
#formula for calculating sum of square of even numbers
evenSqaureSum=4*a*(2*a+1)*(a+1)/6
#Sum of Square of odd terms= Sum of square of all terms - Sum of square of even terms
oddSqaureSum=(n*(n+1)*(2*n+1)/6)-evenSqaureSum
print("Sum of square of even terms =",evenSqaureSum)
print("Sum of square of odd terms =",oddSqaureSum)