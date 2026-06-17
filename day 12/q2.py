# WAP to check if a number is positive, negative, or zero.

num = float(input("Ener a number: "))
if num > 0:
    print(num, "is a positive number.")
elif num < 0:
    print(num, "is a negative number.")
else:
    print(num, "is zero.")