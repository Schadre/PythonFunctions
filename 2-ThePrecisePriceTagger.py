"""
Create a program that rounds off prices to a user-friendly format
"""
def price_is_right():
    num = input("Please input the price of your favorite item including the tax and I will round it off: ")
    num = float(num)
    if num is not int:
        round(num)
    else:
        pass
    print(f"The price rounded is: {round(num)}")
price_is_right()