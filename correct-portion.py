"""
Tung Hoang - 08/28/19

This program computes how many tons of food each person 
in a group should take. Then it will determine whether the
user take the correct portion.
"""

# Amount of food and number of people
tonsOfFood = 0.8
numPeople = 56

# Determine how much food each person gets
tonsOfFoodPerPerson = round(tonsOfFood / numPeople, 5)

print (tonsOfFoodPerPerson)

# Ask the user how much food they took
tonsTaken = float(input("How many tons of food did you take? "))

# Determine if they get the correct portion size
if round(tonsTaken,5) == tonsOfFoodPerPerson :
    print("Good job, you took the right amount of food!")
else:
    print("You took the wrong amount of food!")
