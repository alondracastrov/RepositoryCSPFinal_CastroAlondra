import random

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789#$-_%;\("

while True:
    password_length = int(input("How long would you want your password to be : "))
    passwords_generated = int(input("How many passwords do you want : "))
    for x in range(0,passwords_generated):
        password = ""
        for x in range(0,password_length):
            password_character = random.choice(characters)
            password = password + password_character
        print("Your new password is : ", password)
