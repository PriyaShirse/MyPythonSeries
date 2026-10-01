try:
    age = int(input("Enter Your Age:"))
except ValueError:
    print("Enter Only Number")
else:
    print("Age is", age)