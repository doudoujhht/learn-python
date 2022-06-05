import random
import string
print("welcome to my password generator")
nbOfLetter = int(input("how many letters do you want in your password? "))
nbOfDigit = int(input("how many digits do you want in your password? "))
nbOfSpecialChar = int(input("how many special characters do you want in your password? "))
password = ""
for i in range(nbOfLetter):
    password+=random.choice(string.ascii_letters)

for i in range(nbOfDigit):
    password+=random.choice(string.digits)

for i in range(nbOfSpecialChar):
    password+=random.choice(string.punctuation)

password = list(password)
random.shuffle(password)
password = "".join(password)
print("your password is: ", password)