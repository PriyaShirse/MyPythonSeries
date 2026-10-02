# Q1. Student Class
# Create a class Student with the properties name, age, and course.
# Create one object and display all details.
class Student:
    name = "Priya"
    age = 21
    course = "Python"


stud = Student()
print(stud.name)
print(stud.age)
print(stud.course)
print("-" * 70)


# Q2. Car Class
# Create a class Car with the properties brand, color, and price.
# Create one object and display the car details.
class Car:
    brand = "BMW"
    color = "Black"
    price = 45000


c1 = Car()
print(c1.brand)
print(c1.color)
print(c1.price)
print("-" * 70)


# Q3. Mobile Class
# Create a class Mobile with the properties brand, price, and storage.
# Create one object and display all properties.
class Mobile:
    brand = "Oppo"  # cspell: disable-line
    price = 50000
    storage = "900ram"


m1 = Mobile()
print(m1.brand)
print(m1.price)
print(m1.storage)
print("-" * 70)


# Q4. Employee Class
# Create a class Employee with the properties name, department, and salary.
# Create an object and display employee details.
class Employee:
    name = "Rohan"
    department = "IT"
    salary = 50000


e1 = Employee()
print(e1.name)
print(e1.department)
print(e1.salary)
print("-" * 70)


# Q5. Book Class
# Create a class Book with the properties title, author, and price.
# Create one object and display the book information.
class Book:
    title = "Python"
    author = "Rahul"
    price = 500


b1 = Book()
print(b1.title)
print(b1.author)
print(b1.price)
print("-" * 70)


# Q6. Student Method
# Create a class Student with a name property and a study() method.
# The method should display: Rahul is studying Python.
class Student:
    name = "Rahul"

    def study(self):
        print(f"{self.name} is studying Python.")


# Create an object and call the method.
s1 = Student()
s1.study()
print("-" * 70)


# Q7. Calculator Class
# Create a class Calculator with two properties: num1 = 10 and num2 = 5.
# Create methods add(), subtract(), multiply(), and divide().
class Calculator:
    num1 = 10
    num2 = 5

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num1 / self.num2


calc = Calculator()
print("Addition:", calc.add())
print("Subtraction:", calc.subtract())
print("Multiplication:", calc.multiply())
print("Division:", calc.divide())
print("-" * 70)


# Q8. Bank Account Class
# Create a class BankAccount with the properties account_holder,
# account_number, and balance.
# Create a method show_details() to display all account details.
class BankAccount:
    account_holder = "Rahul"
    account_number = 123456789
    balance = 10000

    def show_details(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance}")


bank = BankAccount()
bank.show_details()
print("-" * 70)


# Q9. Multiple Objects
# Create a class Student with the properties name, age, and course.
# Create 3 objects: s1 -> Rahul, s2 -> Priya, and s3 -> Amit.
# Display the details of all three students.
class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Course: {self.course}")


s1 = Student("Rahul", 20, "Python")
s2 = Student("Priya", 22, "Java")
s3 = Student("Amit", 21, "C++")

s1.show_details()
s2.show_details()
s3.show_details()
print("-" * 70)


# Q10. Product Class
# Create a class Product with the properties name, price, and quantity.
# Create a method show_product() to display the product details.
# Create 2 objects with different product details and display both.
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def show_product(self):
        print(
            f"Product Name: {self.name}, "
            f"Price: {self.price}, Quantity: {self.quantity}"
        )


p1 = Product("Laptop", 50000, 2)
p2 = Product("Phone", 25000, 5)

p1.show_product()
p2.show_product()
