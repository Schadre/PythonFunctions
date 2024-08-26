""" 
Using f-strings for output, and apply this to a 
practical scenario of temperature conversion
"""

tempurates_in_celsius = [10, 20, 25, 30, 35]

for temperatures in tempurates_in_celsius:
    fahrenheit = (temperatures * 9/5) + 32
    print(f"The Celsius temperature is: {temperatures} and the Fahrenheit temperature is: {fahrenheit}")