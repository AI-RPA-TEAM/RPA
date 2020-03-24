#Q1
print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")

#Q2
import sys
print("Python version")
print (sys.version)

#Q3
import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

#Q4
fname = input("Enter your First Name : ")
lname = input("Enter your Last Name : ")
print (lname + " " + fname)

#Q5
values = input("Please enter some comma seprated numbers : ")
list = values.split(",")
tuple = tuple(list)
print('List  is: ',list)
print('Tuple is: ',tuple)

#Q6
import string
filename=input("Input the file name with extension: ") 
dot= filename.split(".")
print("Extention is: ",dot[1])

#Q7
color_list = ["Red","Green","White" ,"Black"]
print("First colour: ",color_list[1])
print("Last colour: ",color_list[-1])

#Q8
exam_st_date = (11, 12, 2014)
print("The examination will start from :", end="")
print(exam_st_date[0],exam_st_date[1],exam_st_date[2], sep="/")

#Q9
n=input("enter as number: ")
nn=n*2
nnn=n*3
try:
    n=int(n)
    nn=int(nn)
    nnn=int(nnn)
    sum=n+nn+nnn
    print("Result: ",sum)
except:
    print("Entered value is not an integer")

#Q10
print(abs.__doc__)
""" print(pow.__doc__)
print(chr.__doc__)
print(enumerate.__doc__)
print(input.__doc__) """

#Q11
import calendar
yyyy = int(input("Input the year : "))
mm = int(input("Input the month : "))
print(calendar.month(yyyy, mm))

#Q12
print("""
a string that you "don't" have to escape
This
is a  ....... multi-line
heredoc string --------> example
""")

#Q13
from datetime import date
first = date(2014, 7, 2)
last = date(2014, 7, 11)
diff = last - first
print(diff.days)