#1
import datetime
import calendar

Name=input("Give me your Name")
DOB =input("Give me your DOB")
Date=datetime.datetime.strptime(DB,'%d %m %Y')
Day=D.replace(year = Date.year+100)
print("Hello " +Name+ ", You will turn 100 years old in the year" ,Day.year)
N=Day.weekday()
Day_Name= ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
print("Day of your 100th Birthday is ",Day_Name[N])

#2
Number=(int)(input("Enter Number: "))
for x in range(1,Number+1):
    if(Number%x==0):
        print(x)
        
#3
List1= [1, 2, 3, 4, 5,6,11] 
List2= [5, 6, 7, 8, 9,10] 
a=set(List1)
b=set(List2)
      
if len(a.intersection(b)) > 0: 
    print(a.intersection(b))   
else: 
    print("no common elements") 

#4
string = input("Please enter the String : ")
if(string == string[:: - 1]):
   print("This word is a palindrome")
else:
   print("This word is not a palindrome")

#5
import math

class circle():
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * (self.radius ** 2)
    def perimeter(self):
        return 2 * math.pi * self.radius

Radius = int(input("Enter radius of circle: "))
obj = circle(Radius)
print("Area of circle:", round(obj.area(), 2))
print("Perimeter of circle:", round(obj.perimeter(), 2))
