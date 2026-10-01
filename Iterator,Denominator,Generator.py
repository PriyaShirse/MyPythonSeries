# Iterator:
# num = [1, 2, 3, 4, 5]

# my_iterator = iter(num)

# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))

# name = "Python"

# iterName = iter(name)

# print(next(iterName))
# print(next(iterName))
# print(next(iterName))
# print(next(iterName))
# print(next(iterName))
# print(next(iterName))

# marks = [87, 55, 76, 98, 43]

# mark_iter = iter(marks)

# while True:
#     try:
#         print(next(mark_iter))
#     except StopIteration:
#         break

# Generator:

# def num():
#     yield 20
#     yield 30
#     yield 50

# result = num()
# print(next(result))
# print(next(result))
# print(next(result))

# def nums():
#     for i in range(1, 6):
#         yield i
#
# for num in nums():
#     print(num)

# # Find Square of 1 to 5 number

# def Square_Num():
#     for i in range(1, 6):
#         yield i * i

# for num in Square_Num():
#     print(num)

# # Find even numbers from 1 to 10 numbers

# def Even():
#     for i in range(1, 11):
#         if i % 2 == 0:
#             yield i

# for Num in Even():
#     print("Even Numbers are:", Num)

# Decorator:

# EX1
def my_decorator(func):
    def wrapper():
        print("Before Function")
        func()
        print("After Function")

    return wrapper


@my_decorator
def greet():
    print("Hello Student")


greet()


# Ex2

def wel(func):
    def wrapper():
        print("Welcome to clg...!")
        func()

    return wrapper


@wel
def clg():
    print("Login Successfully....!")


clg()


# EX3

def student(func):
    def wrapper():
        print("Function Started")
        func()

    return wrapper


@student
def log():
    print("SuccessFully Login......!")


log()

# Ex4


def msg(func):
    def wrapper():
        print("Before Exam")
        func()
        print("After Exam")

    return wrapper


@msg
def exam():
    print("Exam Started")


exam()
