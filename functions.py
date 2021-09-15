def greet_user():
    print("Hello!")

greet_user()

# Passing information to a function
def greet_user2(username):
    print(username.title())

greet_user2('alexcar')

# Passing arguments
# Positional arguments
def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet('hamster', 'harry')
describe_pet('dog', 'teddy')

# Order matters in positional arguments
describe_pet('teddy', 'dog')

# keyword arguments
describe_pet(animal_type='dog', pet_name='teddy')
describe_pet(pet_name='teddy', animal_type='dog')

# Default values
def describe_pet2(pet_name, animal_type='dog'):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet2(pet_name='willie')
describe_pet2('willie')
describe_pet2(pet_name='harry', animal_type='hamster')

# Return values
# Return a simple value

def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# Making an argument optional
def get_formatted_name(first_name, middle_name, last_name):
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

def get_formatted_name(first_name, last_name, middle_name = ''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

# Returning a dictionary
def build_person(first_name, last_name):
    person = {'first': first_name, 'last': last_name}
    return person

musician =  build_person('jimi', 'hendrix')
print(musician)

def build_person(first_name, last_name, age=None):
    person = {'first': first_name, 'last': last_name}
    
    if age:
        person['age'] = age
    
    return person

musician =  build_person('jimi', 'hendrix', age=27)
print(musician)


# Passing a list
def greet_users(names):
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

# Modifying a list in a function

# Start with some designs that need to be printed.
unprinted_designs = ['phone case', 'robot pendant', 'dodecachedron']
completed_models = []

# Simulate printing each design, until none are left.
# Move each design to completed_models after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

# Display all completed models
print("\n following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left
    Move each design to completed_models after printing
    """

    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed"""
    print("\n following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecachedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# Passing an arbitrary number of arguments
# def make_pizza(*toppings):
#     print("\nMaking a pizza with the following toppings:")
#     for topping in toppings:
#         print(f"- {topping}")

# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')

# Mixing positional and arbitrary arguments
# def make_pizza(size, *toppings):
#     """Summarize the pizza we are about to make"""
#     print(f"\nMaking a {size}-inch pizza with the following toppings:")
#     for topping in toppings:
#         print(f"- {topping}")

# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Using arbitrary keyword arguments
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last

    return user_info

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)
