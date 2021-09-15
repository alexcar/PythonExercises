# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)
# ======================================================

# name: str
# name = input("Please enter your name: ")
# print(f"\nHello, {name}")
# ======================================================

# prompt = "If you tell us who you are, we can personalize the messages you see."
# prompt += "\nWhat is your first name? "

# name: str
# name = input(prompt)
# print(f"\nHello, {name}")
# ======================================================

# height = input("How tall are you, in inches? ")
# height = int(height)

# if height >= 48:
#     print("\nYou're tall enough to ride!")
# else:
#     print("\nYou'll be able to ride when you're a littel older.")

# ======================================================

# Introduction while loops
# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1

# ======================================================

# Letting the user choose when to quit 
# prompt = "\nTell me something, and I will repeat it back to you:" 
# prompt += "\nEnter 'quit' to end the program. "

# message = ""
# while message != 'quit':
#     message = input(prompt)
    
#     if message != 'quit':
#         print(message)

# ======================================================

# prompt = "\nTell me something, and I will repeat it back to you:" 
# prompt += "\nEnter 'quit' to end the program. "

# active = True
# while active:
#     message = input(prompt)

#     if message == 'quit':
#         active = False
#     else:
#         print(message)

# ======================================================

# Using break to exit a loop

# prompt = "\nPlease enter the name of a city you have visited:" 
# prompt += "\nEnter 'quit' when you are finished. "

# while True:
#     city = input(prompt)

#     if city == 'quit':
#         break
#     else:
#         print(f"I'd love to go to {city.title()}!")

# ======================================================

# Using continue in a loop
# current_number = 0
# while current_number < 10:
#     current_number += 1

#     if current_number % 2 == 0:
#         continue

#     print(current_number)

# ======================================================

# Avoiding infinite loops
# x = 1
# while x <= 5:
#     print(x)
#     x += 1

# ======================================================

# Using a while loop with lists and dictionaries
# Start with users that need to be verified,
# and an empty list to hold confirmed users.
# unconfirmed_users = ['alice', 'brian', 'candace']
# confirmed_users = []

# # Verify each user until there are no more unconfirmed users.
# # Move each verified user into the list of confirmed users.
# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()

#     print(f"Verifing user: {current_user.title()}")
#     confirmed_users.append(current_user)

# # Display all  confirmed users.
# print("\nThe following users have been confirmed:")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())

# # Removing all instances of specific values from a list
# pets = ['dog', 'cat', 'rabbit', 'cat']
# print(pets)

# while 'cat' in pets:
#     pets.remove('cat')

# print(pets)

# ======================================================
# Filling a dictionary with user input

responses = {}

# Set a flag to indicate that polling is active
polling_active = True

while polling_active:
    # Prompt for the person's name and response
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # Store the response in the dictionary
    responses[name] = response

    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let anothet person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False
    
# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")

