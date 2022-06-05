from secrets import choice


choices = input("choose 0 for rock 1 for paper 2 for scissors: ")
bot = choice(["rock", "paper", "scissors"])
print("bot chose", bot)
if choices == "0":
    if bot == "rock":
        print("draw")
    elif bot == "paper":
        print("bot wins")
    else:
        print("player wins")

if choices == "1":
    if bot == "rock":
        print("player wins")
    elif bot == "paper":
        print("draw")
    else:
        print("bot wins")

if choices == "2":
    if bot == "rock":
        print("bot wins")
    elif bot == "paper":
        print("player wins")
    else:
        print("draw")