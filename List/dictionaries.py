"""Dictionaries"""

from typing import Any

alien_0: dict[str, Any]
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

# Adding new key-value pairs
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Starting with an empty dictionary
alien_1: dict
alien_1 = {}

alien_1['color'] = 'green'
alien_1['points'] = 5
print(alien_1)

# Modifying values in a dictionary
alien_1['color'] = 'blue'
print(alien_1)

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")

# Removing key-value pairs
alien_0 = {'color': 'blue', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)

# A dictionary of similar objects
favorite_language: dict[str, str]
favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'alex': 'c#'
}

language: str
language = favorite_language['alex'].title()
print(f"Alex's favorite language is {language}.")

# Using get() to access values
language = favorite_language.get('mary', 'No user value assigned.')
print(language)

# Looping through a dictionary
user_0 = {
    'username': 'alexcar',
    'first': 'alex',
    'last': 'car'
}

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

print('\n')

for name, language in favorite_language.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

# Looping through all the keys in a dictionary
for name in favorite_language.keys():
    print(name.title())

print('\n**************\n')

friends: list[str]
friends = ['phil', 'sarah']

for name in favorite_language.keys():
    print(name.title())

    if name in friends:
        language = favorite_language[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

# Looping through a dictionary's keys in a particular order
# Starting in python 3.7
for name in sorted(favorite_language.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

# Lopping through all values in a dictionary
for language in favorite_language.values():
    print(language.title())

print('\n**************\n')

# Nesting - A list of dictionaries
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

print('\n**************\n')

# Make an empty list for storing aliens
aliens = []

# make 30 green aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Show the first aliens
for alien in aliens[:5]:
    print(alien)

# Show how many aliens have been created
print(f"\nTotal number of aliens: {len(aliens)}")

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

for alien in aliens[:5]:
    print(alien)

print('\n**************\n')

# A list in a dictionary
# Store information about a pizza being ordered
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}

# Summarize the order
print(f"You ordered a {pizza['crust']}-crust pizza with the followinf toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")

# A dictionary in a dictionary
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name}")
    print(f"\tLocation: {location.title()}")

