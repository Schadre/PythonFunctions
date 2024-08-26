""" 
Use the min() and max() functions in Python to find the highest and 
lowest values in a list, and apply this to a practical senario
of determining room temperatures.
"""
room_temperature = [22, 24, 19, 21]
room_names = ["living room", "kitchen", "bedroom", "bathroom"]

warmest_temp = max(room_temperature)
coolest_temp =min(room_temperature)

warmest_room_index = room_temperature.index(warmest_temp)
coolest_room_index = room_temperature.index(coolest_temp)

warmest_room = room_names[warmest_room_index]
coolest_room = room_names[coolest_room_index]

print(f"The warmest room is {warmest_room} at a temperature of {warmest_temp} and the coolest room is {coolest_room} at a temperature of {coolest_temp}")