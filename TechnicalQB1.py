# Q1. Reverse a Number
# Write a Python program to reverse a number without converting it into a
# string.
# Input: 12345
# Output: 54321
num = int(input("Enter Your Number: "))
reverse = 0

while num > 0:
    digit = num % 10
    reverse = (reverse * 10) + digit
    num //= 10

print(reverse)

# Q2. Find the Second Largest Number
# Find the second-largest number in a list without using sort() or sorted().
# Input: [10, 25, 8, 45, 30]
# Output: 30
numbers = [10, 25, 8, 45, 30]
first = second = float("-inf")

for value in numbers:
    if value > first:
        second = first
        first = value
    elif value > second and value != first:
        second = value

print(second)

# Q3. Check Palindrome Number
# Check whether a given number is a palindrome.
# Input: 121
# Output: Palindrome
num = int(input("Enter a number: "))
temp = num
reversed_num = 0

while num > 0:
    digit = num % 10
    reversed_num = (reversed_num * 10) + digit
    num //= 10

if temp == reversed_num:
    print("Palindrome")
else:
    print("Not a palindrome")

# Q4. Count Vowels in a String
# Count the total number of vowels in a given string.
# Input: "Education"
# Output: 5
string = input("Enter Your String: ").lower()
count = 0

for ch in string:
    if ch in "aeiou":
        count += 1

print(count)


# Q5. Find Factorial Using Recursion
# Write a recursive function to calculate the factorial of a given number.
# Input: 5
# Output: 120

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


num = int(input("Enter a number: "))
print(factorial(num))

# Q6. Remove Duplicate Elements
# Remove duplicate elements from a list without using set().
# Input: [1, 2, 3, 2, 4, 1, 5]
# Output: [1, 2, 3, 4, 5]
values = [1, 2, 3, 2, 4, 1, 5]
result = []

for item in values:
    if item not in result:
        result.append(item)

print(result)

# Q7. Find the Missing Number
# A list contains numbers from 1 to 10, but one number is missing.
# Write a program to find it.
# Input: [1, 2, 3, 4, 6, 7, 8, 9, 10]
# Output: 5
numbers = [1, 2, 3, 4, 6, 7, 8, 9, 10]
expected_sum = sum(range(1, 11))
actual_sum = sum(numbers)
print(expected_sum - actual_sum)

# Q8. Character Frequency Counter
# Count the frequency of each character in a string using a dictionary.
# Input: "banana"
# Output: b: 1    a: 3    n: 2
text = "banana"
frequency = {}

for ch in text:
    frequency[ch] = frequency.get(ch, 0) + 1

for key, value in frequency.items():
    print(f"{key}: {value}")

# Q9. Find Common Elements
# Find common elements between two lists without using set().
# Input: A = [1, 2, 3, 4, 5] B = [3, 4, 5, 6, 7]
# Output: [3, 4, 5]
A = [1, 2, 3, 4, 5]
B = [3, 4, 5, 6, 7]
common = []

for item in A:
    if item in B and item not in common:
        common.append(item)

print(common)

# Q10. Sort a List Without Built-in Methods
# Sort a list in ascending order without using sort() or sorted().
# Input: [5, 2, 8, 1, 3]
# Output: [1, 2, 3, 5, 8]
arr = [5, 2, 8, 1, 3]

for i in range(len(arr)):
    for j in range(0, len(arr) - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print(arr)

# Q11. Find the First Non-Repeating Character
# Find the first character that appears only once in a string.
# Input: "aabbcde" Output: c
string = "aabbcde"
frequency = {}

for ch in string:
    frequency[ch] = frequency.get(ch, 0) + 1

for ch in string:
    if frequency[ch] == 1:
        print(ch)
        break
else:
    print("No non-repeating character")

# Q12. Flatten a Nested List
# Convert a nested list into a single list.
# Input: [[1, 2], [3, 4], [5, 6]]
# Output: [1, 2, 3, 4, 5, 6]
nested_list = [[1, 2], [3, 4], [5, 6]]
flat_list = []

for sublist in nested_list:
    flat_list.extend(sublist)

print(flat_list)

# Q13. Find All Prime Numbers in a Range
# Print all prime numbers between 1 and 50.
# Output: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47
primes = []

for candidate in range(2, 51):
    is_prime = True
    for divisor in range(2, int(candidate ** 0.5) + 1):
        if candidate % divisor == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(candidate)

print(primes)

# Q14. Find the Largest Word in a Sentence
# Find the longest word in a sentence.
# Input: "Python programming is very interesting"
# Output: programming
sentence = "Python programming is very interesting"
words = sentence.split()
longest = words[0]

for word in words[1:]:
    if len(word) > len(longest):
        longest = word

print(longest)

# Q15. Merge Two Dictionaries
# Merge two dictionaries into one without using the update() method.
# Input: A = {"a": 1, "b": 2} B = {"c": 3, "d": 4}
# Output: {"a": 1, "b": 2, "c": 3, "d": 4}
A = {"a": 1, "b": 2}
B = {"c": 3, "d": 4}
merged = {}

for key, value in A.items():
    merged[key] = value
for key, value in B.items():
    merged[key] = value

print(merged)

# Q16. Create a Custom Iterator
# Create a custom iterator class that generates numbers from 1 to 10 using
# __iter__() and __next__().
class NumberIterator:
    def __init__(self, limit=10):
        self.limit = limit
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.limit:
            raise StopIteration
        value = self.current
        self.current += 1
        return value

for num in NumberIterator():
    print(num)

# Q17. Create a Generator Function
# Write a generator function using yield that generates the squares of numbers
# from 1 to N.
# Input: 5
# Output: 1, 4, 9, 16, 25
def square_generator(n):
    for i in range(1, n + 1):
        yield i * i

n = int(input("Enter Your Number: "))
for square in square_generator(n):
    print(square)
