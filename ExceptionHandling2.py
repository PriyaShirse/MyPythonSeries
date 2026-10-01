# Types of Error:
#     1.ZeroDivisionError
try:
    num1=34
    num2=0
    
    result=num1/num2
    print(result)
except ZeroDivisionError:
    print("Cannot allow divide by Zero")
        
#     2.ValueError
try:
    age=int(input("Enter Your Age:"))
    print("Age:",age)
except ValueError:
    print("Enter only Integers")  
    
#    - 3.TypeError
try:
    result="45"+35
    print(result)
except TypeError:
    print("Cannot Add str or Integer")
    
#     4.IndexError

list=["a","b","c","d","e"]

try:
    print(list[5])
    
except IndexError:
    print("Element is not present")
    
#     5.NameError
num1=65
try:
    print(num2)
except NameError:
    print("Num2 is not defined")

#     6.FileNotFoundError
try:
    file=open("Index.txt","r")
except:
    print("File not found")
    
#     7.KeyError
dict={
    "name":"priya",
    "age":21
}
try:
    print(dict["city"])
except KeyError:
    print("Not in dict")
