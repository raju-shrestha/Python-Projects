#Human & Computer
#Player move
#Human move
#Tie or Win or Lose
#r = rock, p = paper, s = scissor

import random
moves = ['r', 'p','s']
player_wins = ['pr','sp', 'rs']
tries = 0

while True:

    player_move = input("Your move r or p or s: ")
    if player_move =='q':
        break

    computer_move = random.choice(moves)
    tries = tries+1

    print("You : ", player_move)
    print("Me: ", computer_move)

    if player_move == computer_move:
        print("Tie!")
    elif player_move + computer_move in player_wins:
        print("You win!")
    else:
        print("You lose!")
print("Number of tries", tries)


