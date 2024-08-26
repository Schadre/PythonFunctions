""" 
Use type conversion functions such as int(), float(), str(), and bool()
You will also use loops to iterate over questions and list to store quiz data.
"""

questions = [
    "What is 10 plus 4?",
    "Enter a decimal number between 1 and 2",
    "What is the string representation of the number 20?",
    "Is Python a programming language? (True/False)"
]

correct_answers = [14, 1.5, "20", True]
answer_types = [int, float, str, bool]

score = 0

for i in range(len(questions)):
    user_answer = input(questions[i] + " ")
    try:
        if answer_types[i] == bool:
            converted_answer = user_answer.lower() in ['true', 't', '1', 'yes', 'y']
        else:
            converted_answer = answer_types[i](user_answer)
        if converted_answer == correct_answers[i]:
            print("Correct!")
            score += 1
        else:
            print("Wrong answer.")
    except ValueError:
        print("Invalid input type.")

print(f"Your final score is {score}/{len(questions)}")