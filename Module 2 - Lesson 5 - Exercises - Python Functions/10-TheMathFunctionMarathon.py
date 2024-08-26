""" 
Apply varios mathematical functions such as 
sum(), round(), sqrt(), ceil() and floor()
"""
import math

numbers = [2.5, 3.6, 4.7, 5.8, 6.9]

total_sum = sum(numbers)
print(f"The sum of the numbers is: {total_sum}")

average = total_sum / len(numbers)
print(f"The average is: {average}")

for number in numbers:
    sqrt_number = math.sqrt(number)
    rounded_number = round(sqrt_number)
    if rounded_number < sqrt_number:
        rounded_number = math.ceil(sqrt_number)
    else:
        rounded_number = math.floor(sqrt_number)
    
    if rounded_number > average:
        print(f"{rounded_number} is above the average.")
    elif rounded_number < average:
        print(f"{rounded_number} is below the average.")