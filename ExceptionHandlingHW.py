# 1.Write a python program that handles a ValueError when the user enter text instead of a number.
try:
    num=int(input("Enter a Number:"))
    print(num)
except ValueError:
    print("Please Enter the Number...!")

# 2.Write a python program to divide two numbers and handle the ZeroDivisionError
try:
    num1=34
    num2=0
    result=num1/num2
    print(result)
except ZeroDivisionError:
    print("ZeroDivisionError Do not divide any number by zero")
    
# 3. Write a Python program that handles a TypeError when incompatible data types are used in an operation.
try:
    result="34"+45
    print(result)
except TypeError:
    print("TypeError:You cannot add str and int")
    
# 4. Write a Python program that accesses an invalid list index and handles the IndexError.
list = [1,32,54,67]

try:
    print(list[4])
except IndexError:
    print("Invalid index")
    
    
# 5. Write a Python program that accesses a missing dictionary key and handles the KeyError.
dict1={
    "Name": "Rahul",
    "Age": 21
    }
try:
    print(dict1["City"])
except KeyError:
    print("Invalid Key")
    
    
# 6. Write a Python program to open a file and handle the FileNotFoundError if the file does not exist.
try:
    file=open("File.txt","r")
except FileNotFoundError:
    print("FileNotFound")
    
# 7. Write a Python program using try and except to accept a student's marks and handle invalid input.
try:
    print("Enter Your Marks:")
    Math=int(input("Math Marks"))
    Eng=int(input("Eng Marks"))
    Sci=int(input("Sci Marks"))
except ValueError:
    print("Please enter valid data")
    
# 8. Write a Python program using try, except, and else to calculate the total price of a product.

try:
    price=int(input("Enter the Price:"))
    Quantity=int(input("Enter quantity:"))
except ValueError:
    print("ValueError")
else:
    print("Total=",price*Quantity)
    
# 9. Write a Python program using try, except, and finally to perform a division operation and display a message that the operation is completed.

try:
    num1=int(input("Enter first Number:"))
    num2=int(input("Enter Second Number:"))
    
    print("Division is",num1/num2)
except ZeroDivisionError:
    print("Cannot Divide any number by 0")
finally:
    print("Operation is completed")
    
# 10. Write a Python program using try, except, else, and finally for a simple user registration process.
try:
    email=input("Enter Your Email:")
    password=input("Enter Your Password:")
except:
    print("You have to Register again")
finally:
    print("Successfully Registered......!")
    
# 11. Write a Python program using raise to generate an exception if the user's age is less than 18.
try:
    age=16

    if age<18:
        raise ValueError("Invalid Age")
except ValueError as error:
    print(error)
else:
    print("Age is Accepted..!")
    
# 12. Write a Python program using raise to check whether a password contains at least 8 characters. Raise an exception if it does not.
try:
    password=int(input("Enter Your Password:"))
    if len(password):
        raise Exception("Please Enter Atleast 8 Characters")
    print("Password is Valid")
except ValueError:
    print("Invalid Password.........!")
    
# 13. Write a Python program that accepts a product quantity and uses raise if the quantity is zero or negative.
try:
    quantity=int(input("Enter Your Quantity:"))
    if quantity<0:
        raise Exception("You should enter only positive numbers")
    
except ValueError:
    print("Quantity is zero or negative")
    
# 14. Write a Python program to accept a student's marks and use raise to generate an exception if the marks are greater than 100 or less than 0.

try:
    marks=int(input("Enter your Marks:"))
    
    if marks>100 and marks<0:
        raise ValueError("the marks are greater than 100 or less than 0")
except ValueError:
    print("Please Enter valid marks.")
    
# 15. Write a Python program for a simple bank withdrawal system using try, except, else, finally, and raise. Raise an exception if the withdrawal amount is greater than the available balance.
