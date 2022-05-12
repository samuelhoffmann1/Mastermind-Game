"""Reviewed by Adam at the STC"""
import Dice
import Beetle

"""Get Player Names"""
player1 = Beetle.beetle(1)
player2 = Beetle.beetle(2)
player3 = Beetle.beetle(3)
player4 = Beetle.beetle(4)


"""Function of Game"""
def game(player):
    """While Needed Pieces are Not Met Keep Rolling Die"""
    while player.body < 1 or player.head < 1 or player.legs < 6 or player.eyes < 2 or player.antenna < 2 or player.wings < 2:
        """Obtain Body First"""
        dice = roll.roll()
        if player.body == 0:
            while dice != 6:
                player.turns += 1
                dice = roll.roll()
            player.body += 1
            """When Body is Required Roll for the Rest"""
        else:
            if dice == 3:
                player.turns += 1
                player.legs += 1
            elif dice == 6:
                player.body += 1
                player.turns += 1
            elif dice == 5:
                player.head += 1
                player.turns += 1
            elif dice == 4:
                player.turns += 1
                player.wings += 1
            elif dice == 1 and player.head == 0:
                player.turns += 1
            elif dice == 2 and player.head == 0:
                player.turns += 1
            elif dice == 1 and player.head != 0:
                player.turns += 1
                player.eyes += 1
            elif dice == 2 and player.head != 0:
                player.turns += 1
                player.antenna += 1
"""Reset Beatle Class for More Games"""
def reset(player):
    player.body = 0
    player.head = 0
    player.legs = 0
    player.eyes = 0
    player.antenna = 0
    player.wings = 0
    player.turns = 0

flag = "y"
"""Main"""
while flag == "y":
    reset(player1)
    reset(player2)
    reset(player3)
    reset(player4)

    seed = input("What is the Seed? ")
    roll = Dice.dice(seed)

    game(player1)
    game(player2)
    game(player3)
    game(player4)
    """Create Dictionary of Names and Players"""
    winner = {
        player1.name : player1.turns,
        player2.name : player2.turns,
        player3.name : player3.turns,
        player4.name : player4.turns
    }
    """Find Least Amount of Turns"""
    all_values = winner.values()
    min_value = min(all_values)
    """End Format"""
    print()
    print("Seed Player Turns")
    print("-------------------")
    print("{}   {}    {}".format(seed, min(winner, key=winner.get), min_value)
    )
    flag = input("Would you like to play again? (y/n) ")

print("Thanks for Playing!")
