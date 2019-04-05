import random

def eval_winner(p1, p2):
    """
    This function accepts two integers, p1 and p2, and calculates who wins based on a game of RPS

    1 = Rock
    2 = Paper
    3 = Scissors
    """

    switch = {
            1: "Rock",
            2: "Paper",
            3: "Scissors"}
    if((p1 == 1 and p2 == 3) or (p1 == 2 and p2 == 1) or (p1 == 3 and p2 == 2)):
        print("P1 threw " + switch.get(p1))
        print("P2 threw " + switch.get(p2))
        return 1
    elif((p2 == 1 and p1 == 3) or (p2 == 2 and p1 == 1) or (p2 == 3 and p1 == 2)):
        print("P1 threw " + switch.get(p1))
        print("P2 threw " + switch.get(p2))
        return 2
    else:
        print("P1 threw " + switch.get(p1))
        print("P2 threw " + switch.get(p2))
        return 0

#main

wins = 0
losses = 0
draws = 0
round_number = 1
while True:
    p2 = random.randint(1,3)
    print ("Round " + str(round_number))
    print ("Pick Rock, Paper, Scissors, or Quit")
    print ("('r', 'p', 's', or 'q')")
    x = input()

    if(x == "R" or x == "r"):
        w = eval_winner(1,p2)
        if (w == 0):
            draws += 1
            print ("DRAW!")
        elif (w == 1):
            wins += 1
            print ("you win!")
        else:
            losses += 1
            print ("you lost...")
        print ("Wins: " + str(wins) + "; Losses: " + str(losses) + "; Draws: " + str(draws))
        round_number +=1
        continue
    elif(x == "P" or x == "p"):
        w = eval_winner(2,p2)
        if (w == 0):
            draws += 1
            print ("DRAW!")
        elif (w == 1):
            wins += 1
            print ("you win!")
        else:
            losses += 1
            print ("you lost...")
        print ("Wins: " + str(wins) + "; Losses: " + str(losses) + "; Draws: " + str(draws))
        round_number +=1
        continue
    elif(x == "S" or x == "s"):
        w = eval_winner(3,p2)
        if (w == 0):
            draws += 1
            print ("DRAW!")
        elif (w == 1):
            wins += 1
            print ("you win!")
        else:
            losses += 1
            print ("you lost...")
        print ("Wins: " + str(wins) + "; Losses: " + str(losses) + "; Draws: " + str(draws))
        round_number +=1
        continue
    elif(x == "Q" or x == "q"):
        break
    else:
        print("INVALID, please use proper input.")
        continue
