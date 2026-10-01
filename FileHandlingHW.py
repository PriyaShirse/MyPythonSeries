# 1.Create a file named data.txt and write your name in it using w mode.
file = open("Data.txt", "w")
file.write("Priya")
file.close()

# 2 Create a file named student.txt and write your Name, Age, and City in separate lines.

file = open("Student.txt", "w")
file.write("Name:Priya\n")
file.write("Age:21\n")
file.write("City:Ahilyanagar\n")
file.close()

# 3 Read and print the complete content of a file using read().
file = open("Data.txt", "r")
data = file.read()
print(data)
file.close()

# 4 Read only the first line from a file using readline().
file = open("Student.txt", "r")
data = file.readline()
print(data)
file.close()

# 5 Read the first three lines from a file using readline().
file=open("Student.txt","r")
data=file.readline()
print(data)
data=file.readline()
print(data)
data=file.readline()
print(data)

# 6 Read all lines from a file using readlines() and print them using a for loop.
file=open("Student.txt","r")
data=file.readlines()
for line in data:
    print(line)
file.close()

# 7 Add your course name at the end of an existing file using a mode.
file=open("Student.txt","a")
file.write("course:Python\n")
file.close()

# 8 Create a file and write the names of 5 students into it.
file=open("StudentInfo.txt","w")
file.write("Priya\n")
file.write("Aniket\n")
file.write("Aparna\n")
file.write("Rahul\n")
file.write("Amit\n")
file.close()

# 9 Read a file containing 5 student names and print each name separately.
file=open("StudentInfo.txt","w")
data=file.write("Priya\n")
print(data)
data=file.write("Aniket\n")
print(data)
data=file.write("Aparna\n")
print(data)
data=file.write("Rahul\n")
print(data)
data=file.write("Amit\n")
print(data)
file.close()

# 10 Create a file using x mode and write Welcome to Python into it.
file=open("CreateFile2.txt","x")
file.write("Welcome to Python")
file.close()

# 11 Using w mode, write three programming languages into a file and then read the file.
file=open("MyFile.txt","w")
file.write("Python\n")
file.write("Java\n")
file.write("CPP\n")
file.close()

# 12 Add three new student names to an existing file without deleting the old data.
file=open("StudentInfo.txt","a")
file.write("Shamika\n")
file.write("Rohini\n")
file.write("Sakshi\n")
file.close()

# 13 Use the with keyword to open a file and print all its content.

# 14 Create a file containing marks of 5 students. Read all the lines and display them one by one.
file=open("Marks.txt","r")
data=file.readline()
print(data)
data=file.readline()
print(data)
data=file.readline()
print(data)
data=file.readline()
print(data)
file.close()

# 15 Write a program using with open() that creates a file named message.txt, writes Python File Handling is Easy into it, and then reads and prints the content.

with open("message.txt","x") as file:
    file.write("Python File is easy to handle")
    print("Python File is easy to handle")
    file.close()