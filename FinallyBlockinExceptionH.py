try:
    age = int(input("Enter Your Age:"))
    print(age)
except ValueError:
    print("age is invalid")
finally:
    print("Thank you for visiting.....!")