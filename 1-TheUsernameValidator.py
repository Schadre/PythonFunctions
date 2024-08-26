"""
Create a program that validates usernames based on length. 
This exercise will focus on using conditional statements and the len() function.
"""

def validator():
    username = input(str("What would you like to make your username?"))
    if len(username) >= 5:
        print(f"Your Username: {username} is valid!")
    else:
        print(f"Your Username: {username} is not acceptable.")
validator()