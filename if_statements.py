'''
Created on Jan 7, 2019

@author: justine
'''

# IF STATEMENTS
cars = ["audi", "bmw", "subaru", "toyota"]

for car in cars:
    if car == "bmw":
        print(car.upper())
    else: 
        print(car.title())

requested_topping = "mushrooms"
if requested_topping != "anchovies":
    print("\nHold the anchovies!\n")
    
age = 20
if age < 21 and age > 18:
    print("You are younger than 21 and older than 18!\n")
    
age = 20
if age < 21 or age > 18:
    print("You are younger than 21 or older than 18!\n")
    
banned_users = ["Justine", "Robert"]
user = "Andrew"
if user not in banned_users:
    print(user + " is not a banned user!\n\n")


# IF, ELIF, ELSE    
age = 18

if age < 4:
    print("Your admission is free!")
elif age >= 4 and age < 18:
    print("Your admission is $5")
else:
    print("Your admission is $10")

# PYTHON DOES NOT REQUIRE AN ELSE BLOCK
# CAN HAVE MULTIPLE ELIF BLOCKS