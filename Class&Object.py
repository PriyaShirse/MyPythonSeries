# syntax:
'''class ClassName:
    pass
s1 = ClassName(parameters)
'''

# Example:


# 1
class student:
    name = "Priya"
    age = 21


s1 = student()

print(s1.name)
print(s1.age)


# 2
class emp:
    name = "Rohan"
    age = 25


e1 = emp()
e2 = emp()
print(e1.name)
print(e2.age)


# 3
class stud1:
    clg = "DVVPCOE"


s1 = stud1()
s2 = stud1()
s3 = stud1()
s4 = stud1()

print(s1.clg)
print(s2.clg)
print(s3.clg)
print(s4.clg)


# 4
class emp1:
    pass


e1 = emp1()
e2 = emp1()

e1.name = "Rohan"
e2.name = "Priya"

print(e1.name)
print(e2.name)