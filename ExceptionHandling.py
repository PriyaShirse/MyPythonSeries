#Exception Handling 

#Exception handling is a mechanism to handle runtime errors, allowing the program to continue its execution instead of crashing.
#In Python, exceptions can be handled using try and except blocks.

#  Types of Errors:

#1.ZeroDivisionError:If we try to divide a number by zero ,then we got zero division error.
try:
    a=10
    b=0
    
    c=a/b
    print(c)
except ZeroDivisionError:
    print("Something Went Wrong")
    
#2.ValueError:If we try to convert a string into integer then we got value error.

try:
    age=int(input("Enter your age:"))
    print(age)
except ValueError:
    print("Enter Only Numbers")
    
#3.TypeError:If we have a string and we try to add it with integer then we got type error.
try:
    a=23
    b="Priya"
    
    c=a+b
    print(c)
    
except TypeError:
    print("Please Enter Same Data Type")
    
#4.IndexError:IF we try to access an error which is not present in list then we got index error.

list=[10,20,30,40,50]
try:
    print(list[7])
except IndexError:
    print("Index is not present in list")
    
#5.KeyError:If we try to accesss a key which is not present in dictionary then we got key error.
dict={"Name":"Priya","Age":23}

try:
    print(dict["City"])
except KeyError:
    print("KeyError")
    
#6.NameError:If we try to access a variable which is not defined then we got name error.

try:
    print(m)
except NameError:
    print("a is not defined")
    
#7.FileNotFoundError:If we try to access a file which is not present in the directory then we got file not found error.
try:
    file=open("Priya.txt","r")
except FileNotFoundError:
    print("File Not Found")