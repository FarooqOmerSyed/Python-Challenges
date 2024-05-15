import random


def user_name():
    email = input("Enter your email: ")
    for char in email:
        if char == '@':
            # Generate a random number between 100 and 999
            random_number = random.randint(100, 999)
            return email[:email.index('@')] + str(random_number)


username = user_name()
print("Username with random number:", username)