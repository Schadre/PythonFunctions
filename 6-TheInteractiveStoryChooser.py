""" 
Use the input() function to capture user input, along with conditional statements 
to direct the flow of a program, and list to store and manipulate data
"""

print("You wake up in a mysterious forest. Two paths lie before you. ")

choices = ["left", "right"]
outcomes = ["You encounter a friendly elf who offers you a map.", "You stumble upon a sleeping dragon"]

print(f"Do you go left or right? (Type 'left' or 'right')")
decision = input().lower()

if decision not in choices:
    print("Confused, you decide to wait for a clearer sign of which path to take.")
elif decision == 'left':
    outcome_index = choices.index('left')
    print(outcomes[outcome_index])
else: 
    outcome_index = choices.index('right')
    print(outcomes[outcome_index])