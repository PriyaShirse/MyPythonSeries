# Pillars of OOP:
'''1.Class
    2.Object
    3.Inheritance
    4.Polymorphism
    5.Encapsulation
    6.Abstraction
'''

# Ex1


class Car:
    name = "Thar"
    color = "Black"
    model = "2023"

    def start(self):
        print("Car is starting")

    def stop(self):
        print("Car is stopping")


c1 = Car()

print(c1.name)
print(c1.color)
print(c1.model)

c1.start()
c1.stop()

# Ex2


class Student:
    def toppers(self):
        print("Is the topper")

    def average(self):
        print("Is the average student")


std = Student()
std.name = "Rahul"
std.age = 21

print(std.name)
print(std.age)
std.toppers()

std2 = Student()
std2.name = "Priya"
std2.age = 22

print(std2.name)
print(std2.age)
std2.average()


# Ex3


class Car1:
    def start(self):
        print("Car is Started")

    def stop(self):
        print("Car is Stopped")


creta = Car1()
creta.name = "Creta"
creta.color = "White"
print(creta.name)
print(creta.color)
creta.start()
creta.stop()

print("************************************")

thar = Car1()
thar.name = "Thar"
thar.color = "Black"
print(thar.name)
print(thar.color)
thar.start()
thar.stop()
