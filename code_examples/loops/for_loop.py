# for num in range(1, 10):
#     if num == 5:
#         break # Stops the loop at 5
#     if num % 2 == 0:
#         continue # Skips even numbers
#     print(num)
#
#
# for i in range(3):
#     password = input("Enter password: ")
#     if password == "123":
#         print("Access Granted")
#         break
# else:
#     # This runs only if the loop finished all 3 attempts without a 'break'
#     print("Too many failed attempts.")
#
#
# names = ["Alice", "Bob"]
# scores = [85, 92]
#
# # Using zip to pair lists
# for name, score in zip(names, scores):
#     print(f"{name} scored {score}")
#
# # Using enumerate for indexing
# for index, name in enumerate(names):
#     print(f"User #{index}: {name}")


#Homework №2
# Task 4: The Immutable Coordinates (Tuples)
locations = [(40.7128, -74.0060), (34.0522, -118.2437), (51.5074, -0.1278)]

def showcoordinates(data):
    '''Shows latitude and langtitude'''
    for lat in data:
        lat_lilst = list(lat)
        print("Latitude: [", lat_lilst[0], "], Longtitude: [", lat_lilst[0], "]")

showcoordinates(locations)

#
# list_str = ['n', 'a', 'm', 'e']
#
# name_var = ''
# for list_str in list_str:
#     name_var += list_str
#
# print(name_var)