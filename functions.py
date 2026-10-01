#Syntax
'''def funct_name():     
    //Statement
    
    funct_name()'''


#Examples

#1
def sub(Total,Remaining):
    print("Total_bill=",Total-Remaining)

sub(12000,500)


def bill(price,quantity):
    print("Total=",price*quantity)

bill(200,4)
bill(300,2)


def add(a,b):
    print("Sum=",a+b)
add(10,20)
add(40,10)


def Func(name):
    print("My Name is ",name)
Func("Priya")
Func("Rahul")

def myFun():
    print("Hello World...!")
myFun()


def sub(a,b):
    print("Sub=",a-b)
sub(23,3)

def mul(a,b):
    print("Mul=",a*b)
mul(20,2)

def Div(a,b):
    print("Div=",a/b)
Div(45,9)

def Square(a):
    print("Square of ",a," is",a**2)
Square(2)
Square(7)

def Cube(a):
    print("Cube of ",a," is ",a**3)
Cube(5)

def EvenOdd(num):
    if(num%2==0):
        print("Even")
    else:
        print("Odd")

EvenOdd(3)
EvenOdd(4)


def Check(num1,num2):
    if(num1>num2):
        print(num1,"is max")
    else:
        print(num2," is max")

Check(23,45)

def myNum(num):
    if(num<0):
        print("Num is negative")
    elif(num>0):
        print("Num is positive")
    elif(num==0):
        print("Num is zero")
myNum(4)
myNum(0)
myNum(-4)

def balance1(bal):
    print("Balance:",bal)
balance1(500)

#Default parameterized function

def student_info(name,city,age=21):
    print("Name:",name)
    print("age:",age)
    print("City:",city)

student_info("Priya",21,"Nashik")
student_info("Aparna","Pune")

#Global Variable:Declare variable outside of function

name="priya"
def myName():
    print(name)
myName()

#Local Variable:Declare variable outside of function

def myName():
    name="priya"
    print(name)
myName()
