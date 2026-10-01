# 1

print("Output1")


def wel(Func):
    def wrapper():
        print("Welcome to python...!")
        Func()

    return wrapper


@wel
def greet():
    print("it's greet function...!")


greet()


# 2
print("Output2")


def Start(func):
    def wrapper():
        print("Function started")
        func()

    return wrapper


@Start
def display():
    print("Function Completed")


display()


# 3
print("Output3")


def my_decor(func):
    def wrapper(name):
        print("Welcome")
        func(name)

    return wrapper


@my_decor
def greet(name):
    print(name)


greet("Rahul")


# 4
print("Output4")


def addition(func):
    def wrapper(a, b):
        print("Sum")
        func(a, b)

    return wrapper


@addition
def add(a, b):
    print(a + b)


add(2, 4)


# 5
print("Output5")


def Clg(fun):
    def wrapper(name, marks):
        print("Checking student details...!")
        fun(name, marks)

    return wrapper


@Clg
def stud(name, marks):
    print(name, marks)


stud("Priya", 45)


# 6
print("Output6")


def repeat_decorator(func):
    def wrapper():
        for i in range(3):
            func()

    return wrapper


@repeat_decorator
def hello():
    print("Hello!")


hello()


# 7
print("Output of 7")

