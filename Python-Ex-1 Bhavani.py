#1
print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")

#2
import sys
print("Current Python version")
print (sys.version)

#3
import datetime
DT = datetime.datetime.now()
print ("Current date and time : ")
print (DT.strftime("%Y-%m-%d %H:%M:%S"))

#4
FirstName = input("Enter your First Name : ")
LastName = input("Enter your Last Name : ")
print (LastName + " " + FirstName)

#5
Data = input("Please enter some comma seprated numbers : ")
list = Data.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)

#6
import string
FileName=input("Input the file name with extension: ") 
Separator= FileName.split(".")
print("Extention is: ",Separator[1])

#7
ListofColor = ["Red","Green","White" ,"Black"]
print("First Color: ",ListofColor[1])
print("Last Color: ",ListofColor[-1])

#8
exam_st_date = (11, 12, 2014)
print("The examination will start from :", end="")
print(exam_st_date[0],exam_st_date[1],exam_st_date[2], sep="/")

#9
n1=input("enter a number: ")
n2=n*2
n3=n*3
try:
    n1=int(n)
    n2=int(nn)
    n3=int(nnn)
    Sum=n1+n2+n3
    print("Result: ",Sum)
except:
    print("Entered value is not an integer")

#10
print(abs.__doc__)

#11
import calendar
Year = int(input("Input the year : "))
Month = int(input("Input the month : "))
print(calendar.month(Year, Month))

#12
print("""
a string that you "don't" have to escape
This
is a  ....... multi-line
heredoc string --------> example
""")

#13
from datetime import date
FirstDate = date(2014, 7, 2)
LastDate = date(2014, 7, 11)
Difference = LastDate - FirstDate
print(Difference.days)
	