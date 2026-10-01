# Add two numbers using args


def add_num(*args):
    total = 0

    for number in args:
        total = total + number
    return total

print(add_num(23, 56))


# Bill Calculations
def calculate_Bill(*price):
    total_count = 0
    for Price in price:
        total_count = total_count + Price
    return total_count


print(calculate_Bill(23, 45, 65))

# Calculate marks of student


def Stud_Marks(*Marks):
    total_Marks = 0
    for i in Marks:
        total_Marks = total_Marks + i
        return total_Marks


print(Stud_Marks(90, 45, 56, 65, 54))
