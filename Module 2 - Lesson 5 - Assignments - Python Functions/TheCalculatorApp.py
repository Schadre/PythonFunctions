""" 
Objective: The aim of this assignment is to build a basic calculator 
that can perform addition, subtraction, multiplication, and division.

Task 1: Create functions for each arithmetic operation.

Task 2: Use inputs to ask the user what operation they want to perform, 
and what numbers they want to use.

Task 3: Ensure your code can handle division by zero and other potential errors. 
So if you divide by 0, there is error handling set up to prevent an 
error from showing in the console.
"""

def calculator():
    print("Welcome to the Calculator! ")
    introduction = (str(input("Would you like to Add, Subtract, Multiply, or Divide? \n"))).lower()
    if introduction == "add":
        print("Please input the first number you'd like to add: \n")
        first_add = (int(input("Enter Number here: ")))
        print("Please input the second number you'd like to add: \n")
        second_add = (int(input("Enter Number here: ")))
        total_add = first_add + second_add
        print(f"{first_add} + {second_add} = {total_add}")
    elif introduction == "subtract":
        print("Please input the first number you'd like to subtract: \n")
        first_subtract = (int(input("Enter Number here: ")))
        print("Please input the second number you'd like to subtract: \n")
        second_subtract = (int(input("Enter Number here: ")))
        total_subtract = first_subtract - second_subtract
        print(f"{first_subtract} - {second_subtract} = {total_subtract}")
    elif introduction == "multiply":
        print("Please input the first number you'd like to multiply: \n")
        first_multiply = (int(input("Enter Number here: ")))
        print("Please input the second number you'd like to multiply: \n")
        second_multiply = (int(input("Enter Number here: ")))
        total_multiply = first_multiply * second_multiply
        print(f"{first_multiply} x {second_multiply} = {total_multiply}")
    elif introduction == "divide":
        print("Please input the first number you'd like to divide: \n")
        first_divide = (int(input("Enter Number here: ")))
        print("Please input the second number you'd like to divide: \n")
        second_divide = (int(input("Enter Number here: ")))   
        try:
            total_divide = first_divide / second_divide
            total_divide = int(total_divide)
            print(f"{first_divide} / {second_divide} = {total_divide}")   
        except ZeroDivisionError: 
            print("Dividing any number by zero does not yield a valid result. Try again.")
    else:
        print("Invalid choice, please choose to add, subtract, multiply, or divide? ")

calculator()