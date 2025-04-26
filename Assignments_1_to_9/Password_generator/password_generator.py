import random
import string

def genrated_password(length= 12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password= ''.join(random.choice(characters) for _ in range(length))
    return password

length = int(input("Enter the length of your desired password: "))

password = genrated_password(length)
print("Your Desired Generated Password:", password)