"""write a python functions to reverse a string without slice and without """

def reverse_user_string(usr_str: str) -> str:
    reversed_str = ""
    for char in usr_str:
        reversed_str = char + reversed_str
    return reversed_str


print(reverse_user_string('world hello'))

def reverse_user_string_slice(user_str: str) -> str:
    return user_str[::-1]

print(reverse_user_string_slice('bonjour lemonde'))