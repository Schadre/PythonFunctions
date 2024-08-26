""" 
Use isinstance() and type() to inspect the types of various
elements in a list.
"""

mixed_list = [10, 3.14, 'Python', False, 42, 'Code', 2.718, True]

integers = []
floats = []
strings = []
booleans = []

for element in mixed_list:
    if isinstance(element, int) and not isinstance(element, bool):
        integers.append(element)
    elif isinstance(element, float): 
        floats.append(element)
    elif isinstance(element, str):
        strings.append(element)
    elif isinstance(element, bool):
        booleans.append(element)
    else:
        print(f"Unknown type: {type(element)}")
print(f"Integers: {integers}")
print(f"Floats: {floats}")
print(f"Strings: {strings}")
print(f"Booleans: {booleans}")