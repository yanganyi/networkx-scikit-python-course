# Task 1.4 - 21 Sticks
# there are 21 sticks in sticks
# each player chooses to pick up 1 to 3 sticks
# the player who takes the last (few) sticks wins
# 1.4.1 implements player versus player
# 1.4.2 implements computer versus player

total=21
player=1
while total>0:
    if player==1:
        if total==21:
            total-=1
            print(f"The computer took 1 stick. {total} sticks remaining.")
        else:
            total-=(4-choice)
            print(f"The computer took {4-choice} sticks. {total} sticks remaining.")
        if total==0:
            print("Computer wins!")
        player=2
    else:
        choice=input("How many sticks do you want to take? ")
        try:
            choice=int(choice)
            assert (choice>=1 and choice<=3)==True
            assert (choice<=total)==True
            total-=choice
            print(f"Player took {choice}. {total} sticks remaining.")
            if total==0:
                print(f"Player {player} wins!")
            player=1
        except: print("Invalid quantity")