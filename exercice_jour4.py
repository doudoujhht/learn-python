from random import Random


names =input("enter names separated by commas: ").title().split(",")
name = names[Random().randrange(len(names))]
print(f"{name} should pay for the meal")