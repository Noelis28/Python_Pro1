import random
characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

length = int(input("¿De cuántos caracteres quieres tu contraseña?: "))

password = ""

for i in range(length):
    password = password + random.choice(characters)

print(f'tu contraseña es{password}')