""" 
Use custom separators and endings in the print() function, 
while also incorporating loops to iterate over elements, and 
lists to store data
"""

shopping_list = ["apples", "bananas", "carrots", "bread", "milk"]

seperator = input("Please enter your preferred item separator (e.g., ',', '/', '-'): ")
ending = input("Please enter your preferred ending phrase (e.g., 'End of list', 'That's all!'): ")

print("Your Shopping List: ", end="\n\n")
for item in shopping_list:
    if item == shopping_list[-1]:
        print(item)
    else:
        print(item, end=seperator + " ")
print("\n\n" + ending)
