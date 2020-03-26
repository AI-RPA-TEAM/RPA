#Question 1#
import datetime
name= input("Enter name: ")
dob= input("Enter DOB in dd-mm-yyyy format: ")
dd,mm,yyyy=map(int, dob.split('-'))
hunderedyear=yyyy+100
hundday=datetime.datetime(hunderedyear, mm, dd,00,00,00,00)
print("Hello %s, You will turn 100 years old in the year %s. Day of your 100th Birthday is on %s."%(name,hunderedyear,hundday.strftime("%A")))
#Question 2#
n = int(input("Enter an integer:"))
print("The divisors of the number are:")
for i in range(1,n+1):
    if(n%i==0):
        print(i)
#Question 3#
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = set(a)
d = set(b)
final = c.symmetric_difference(d)
finallist =list(final)
print(finallist)
#Question4#
string = input("Please enter the String : ")
if(string == string[:: - 1]):
   print("This word is a palindrome")
else:
   print("This word is not a palindrome")
#Question5#
import math


class circle():
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius
r = int(input("Enter radius of circle: "))
obj = circle(r)
print("Area of circle:", round(obj.area(), 2))
print("Perimeter of circle:", round(obj.perimeter(), 2))