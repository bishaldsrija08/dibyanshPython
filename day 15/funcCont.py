def sum(a,b):
    sum = a+b
    return sum

result = sum(2,3)
print(result)


# Q: Write a function that takes two numbers as input and returns their product.

def product(x,y):
    return x * y

result = product(2,3)
print(result)


# Q: WAF to take three numbers as input and return their average.

def average(a,b,c):
    return (a + b + c) / 3

result = average(2,3,40)
print(result)

# WAF to calcualte the area of a rectangle. The function should take length and width as input and return the area.

def area(l, b):
    return l * b

l = int(input("Enter the length of the rectangle: "))
b = int(input("Enter the breadth of the rectangle: "))
result = area(l, b)
print(f"The area of the rectangle is: {result}")