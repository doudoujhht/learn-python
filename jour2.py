print("welcome to the tip calculator")
total = float(input("What is the total bill? "))
nbPerson = int(input("How many people? "))
percentage = int(input("what percentage tip would you like to give? "))
tip = total * (percentage/100)
total = total + tip
totalPerPerson = total / nbPerson
print("the total is:{total} each person should pay: , {totalPerPerson}, for a tip of: {tip}".format(total=total, totalPerPerson=totalPerPerson, tip=tip))