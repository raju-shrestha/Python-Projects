#Computer needs to pick a random number
#Player makes a guess
#Compare the guess to the number
#Print out 'To High', 'To Low','You got it'

import random
secret = random.randrange(1,101) #Pick a number between 1 & 100

guess = 0
tries =0
while guess!=secret:
        guess = int(input("Make a guess: "))
        tries = tries + 1

        if guess > secret:
            print("Too High!")
        elif guess < secret:
            print("Too Low!")
        else:
            print("You got it!")
print("Number of treis", tries)

