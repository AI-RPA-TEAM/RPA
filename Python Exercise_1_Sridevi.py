#Question 1#
print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")

#Question 2#
import platform
print(platform.sys.version)

#Question 3#
from datetime import datetime
# datetime object containing current date and time
now = datetime.now()
print("now =", now)
# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)

#Question 4#
fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
print ("Hello  " + lname + " " + fname)

#Question 5#
values = input("Input some comma seprated numbers : ")
list = values.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)

#Quesstion 6#
filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))

#Question 7#
color_list = ["Red","Green","White" ,"Black"]
print("first color: " +color_list[0]+" last color: "+color_list[3])

#Question 8#
exam_st_date = (11,12,2014)
print( "The examination will start from : %i / %i / %i"%exam_st_date)

#Question 9#
n=int(input("Enter a number n: "))
temp=str(n)
t1=temp+temp
t2=temp+temp+temp
comp=n+int(t1)+int(t2)
print("The value is:",comp)

#Question 10#
print(abs.__doc__)
""" print(pow.__doc__)
print(chr.__doc__)
print(enumerate.__doc__)
print(input.__doc__) """

#Question 11#
import calendar
yyyy = int(input("Input the year : "))
mm = int(input("Input the month : "))
print(calendar.month(yyyy, mm))

#Question 12#
print("""
a string that you "don't" have to escape
This
is a  ....... multi-line
heredoc string --------> example
""")

#Question 13#
from datetime import date
first = date(2014, 7, 2)
last = date(2014, 7, 11)
diff = last - first
print(diff.days)