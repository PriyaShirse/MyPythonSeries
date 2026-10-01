# Q1. Write a Python program to print the multiplication table of a given
# number using a while loop.
print("Output of 1:")
num = int(input("Enter Your Number:"))
i = 1
while i <= 10:
    print(i*num)
    i += 1

# Q2. Write a Python program to check whether a given number is a
# palindrome or not.
print("Output of 2:")
num = int(input("Enter a number:"))
temp = num
reversed_num = 0

while num > 0:
    digit = num % 10                  
    reversed_num = (reversed_num * 10) + digit 
    num = num // 10                
if temp == reversed_num:
    print("is a palindrome!")
else:
    print("is not a palindrome!")

# Q3. Write a Python program to remove duplicate elements from a list
# without using set().

# Q4. Write a Python program to count the frequency of each character in a
# given string using a dictionary.


# Q5. Write a Python function that accepts a list of numbers and returns a
# new list containing only the prime numbers.
print("Output of 5:")
list = [1, 2, 3, 4, 5, 6, 7]


def prime():
    for i in list:
        if i % 2 == 0:
            print(i)

prime()

# Q6. Write a Python program to sort a list of numbers in ascending order
# without using the sort() or sorted() functions.
print("Output of 6:")
list1 = [2, 4, 3, 5, 4, 2, 5, 7, 8]

list1.sort()

print(list1)

# Q7. Write a Python program using a decorator to display a message before
# and after executing a function.

# Q8. Write a Python program to create an iterator that returns only the
# even numbers from a given list.
print("Output of 8:")
list2 = [12, 45, 32, 67, 54]
My_iter = iter(list2)

for i in list2:
    if i % 2 == 0:
        print(i, "is Even") 
print(next(My_iter))

# Q9. Write a generator function that generates Fibonacci numbers up to a
# given limit using yield.
print("Output of 9:")
def fibonacci(limit):
    a,b=1,0
    while a < limit:
        yield a
        a,b=b,a+b
for num in fibonacci(50):
    print(num)
            

# Q10. Write a Python program to generate all prime numbers between 1 and 100
# using a generator function.
print("Output of 10:")
def Prime_num():
    for i in range(1, 101):
        if i % 2 == 0:
            yield i

for number in Prime_num():
    print("Prime numbers are", number)