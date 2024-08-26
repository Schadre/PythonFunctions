""" 
Objective: The aim of this assignment is to create a program 
that helps users make a shopping list.

Task 1: Write a function that lets the user add items to a list.

Task 2: Include a function to remove items from the list.

Task 3: Add a function that prints out the entire list in a formatted way.

Note: The goal of this is to be a program. The recommendation is to use a 
while loop that will allow the user to continue to add, remove, and print off 
their shopping list until they decide to "quit", also known as breaking the loop.
"""
shopping_cart = []
print("Welcome to the Shopping expereince of your dreams!")
print("You are able to add, delete, and view anything you desire!")
option = input("Please select your option: (Add/Delete/View)\n").lower()
while True:
    if option == "add":
        add_cart = input("Please enter what you'd like to add: ")
        shopping_cart.append(add_cart)
        print(f"Your {add_cart}, has been added to your cart.")
        print("Please type 'quit' if you'd like to end your shopping spree!")
        option = input("Please select your option: (Add/Delete/View)\n").lower()
    elif option == "delete":
        delete_cart = input("Please enter what you'd like to delete: ")
        shopping_cart.remove(delete_cart)
        print(f"Your {delete_cart}, has been deleted from your cart.")
        print("Please type 'quit' if you'd like to end your shopping spree!")
        option = input("Please select your option: (Add/Delete/View)\n").lower()
    elif option == "view":
        print(f"Here are the items you have in your cart: \n {shopping_cart}")
        print("Please type 'quit' if you'd like to end your shopping spree!")
        option = input("Please select your option: (Add/Delete/View)\n").lower()
    elif option == "quit":
        print(f"Have an awesome day!")
        break
    else:
        print("Invalid input, please try again")
        option = input("Please select your option: (Add/Delete/View)\n").lower()