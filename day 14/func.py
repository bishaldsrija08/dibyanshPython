def greet(): # Define
    print("Hello, welcome to the program!") # bos

greet() # Call the function
greet() # Call the function


# parameters in functions

def greet_user(name): # defining a function with a parameter
    # name = "Dibyansh"
    print(f"Hello, {name}! Welcome to the program!") # Use the parameter
    
greet_user("Dibyansh") # Call the function with an argument


# greet with name and age

def greetUser(name, age): # defining a function with two parameters
    print(f"Hello, {name}! You are {age} years old.") # Use the parameters

greetUser("Dibyansh", 10) # Call the function with arguments
greetUser("Bishal", 25) # Call the function with different arguments