
def play():
    bids ={}
    while True:
        name = input("What's your name? ")
        bid = int(input("What's your bid? $"))
        bids[name]=bid
        stillBiders = input("Are there still biders? (y/n) ")
        if stillBiders == "n":
            break
    
    print("The winner is", max(bids, key=bids.get),"with a bid of", max(bids.values()))
play()


