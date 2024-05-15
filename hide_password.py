def hide_password():
    password = input('Enter your password: ')
    hidden_password = '*' * len(password)
    print(hidden_password)
    return f"your password length is {len(password)}"


print(hide_password())
