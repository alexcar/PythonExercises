"""Lists"""

from typing import List

# Creating a list
bicycles: List[str]
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# Accessing elements in a list
print(bicycles[0].title()) # frist item
print(bicycles[3].title()) # fourth item

# Using individual values froma list
message : str
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)

# Changing, adding and removing elements 

# Modifying elements in a list
motorcycles: List[str]
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles[0] = 'ducati'
print(motorcycles)

# Adding elements to a list
# Append elements to the end of a list
motorcycles.append('honda')
print(motorcycles)

# Start with an empty list and then add items to the list
# using a series of append() calls.
motorcycles2: List[str]
motorcycles2 = []
motorcycles2.append('honda')
motorcycles2.append('yamaha')
motorcycles2.append('suzuki')
print(motorcycles2)

# Inserting element into a list
motorcycles3: List[str]
motorcycles3 = ['honda', 'yamaha', 'auzuki']
motorcycles3.insert(0, 'ducati')
print(motorcycles3)

# Removing elements from a list
# Removing an item using the del statement
del motorcycles3[0]
print(motorcycles3)

# Removing an item using the pop() method
print(motorcycles2)

popped_motorcycle: str
popped_motorcycle = motorcycles2.pop()

print(motorcycles2)
print(popped_motorcycle)

# Popping items from any position in a list
motorcycles4: List[str]
motorcycles4 = ['honda', 'yamaha', 'suzuki']

first_owned: str
first_owned = motorcycles4.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

# Rememer that each time you use pop(), the item you work is no longer stored
# in the list.

# Removing an item by value
motorcycles5: List[str]
motorcycles5 = ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles5.remove('ducati')
print(motorcycles5)

too_expensive: str
too_expensive = 'honda'
motorcycles5.remove(too_expensive)

# Organizing a list
cars: List[str]
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

# The sorted() function lets you display your list in a particular order but 
# doesn't affect the actual order of the list.
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
print(sorted(cars))

# Printing a list in reverse order
cars.reverse()
print(cars)

# Find the length of a list
len(cars)


# Looping through an entire list
magicians: List[str]
magicians = ['alice', 'david', 'carolina']

for magician in magicians:
    print(magician.title())

# Making numerical lists
for value in range(1, 5):
    print(value)

# Using range() to make a list of numbers
numbers: List[int]
numbers = list(range(1, 6))
print(numbers)

even_numbers: List[int] 
even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares: List[int]
squares = []

for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)

# or

squares = []

for value in range(1, 11):
    squares.append(value ** 2)

print(squares)

# Simple statistics with a list of numbers
digits: List[int]
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

min_digit: int
min_digit = min(digits)
print(min_digit)

max_digit: int
max_digit = max(digits)
print(max_digit)

sum_digit: int
sum_digit = sum(digits)
print(sum_digit)

square = []
squares = [value**2 for value in range(1, 11)]
print(squares)

# working with part of a list
# Slicing a list
players: List[str]
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

# Copy a list
my_foods: List[str]
friend_foods: List[str]

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite food are:")
print(friend_foods)

# Tuples
# Tuples is a list of items that cannot change.
# Tuples use parentheses instead of square brackets
dimensions: tuple[int, int]
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# Looping through all values ina a tuple
for dimension in dimensions:
    print(dimension)

# Although you can't modify a tuple, you can assign a new value to a variable
# tha represents a tuple.
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)



