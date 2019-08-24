def beerSong():
    bottleNum = int(input("Enter number of bottles: "))
    bottleToTakeDown = int(input("Enter num of bottles you want to take down: "))
    while bottleNum > 0:
        if bottleNum - bottleToTakeDown > 0:
            print(f"""- {bottleNum} bottle{'s' if bottleNum != 1 else ''} of beer on the wall, {bottleNum} bottle{'s' if bottleNum != 1 else ''} of beer.
      Take {bottleToTakeDown} down and pass it around, {bottleNum - bottleToTakeDown} {'bottle'}{'s' if bottleNum - bottleToTakeDown != 1 else ''} of beer on the wall.""")
        else:
            print(f"""- {bottleNum} bottle{'s' if bottleNum != 1 else ''} of beer on the wall, {bottleNum} bottle{'s' if bottleNum != 1 else ''} of beer.
      Take {bottleNum} down and pass it around, 0 bottle of beer on the wall.""")
        bottleNum -= bottleToTakeDown

beerSong()
