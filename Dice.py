#This section generates random numbers using the "random" module
import random

def roll():
    min_value = 1
    max_value = 6
    roll=random.randint(min_value,max_value)

    return roll

#value = roll ()
#print(value)

#This section shows the number of players
while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players=int(players)
        if 2<= players <= 4:
            print("Must be between 2 -4 players.")
            break
        else:
            print("Players must be b/n 2 - 4...Try agin")  
    else:
        print("Invalid,try again.")

print(players)

max_score = 50
#This section creates the score list for the number of players 
player_scores = [0 for i in range(players)]    #Here we record the total Score 
#print(player_scores)

while max(player_scores) < max_score:

    for player_idx in range(players):
        print("\nPlayer", player_idx + 1, "turn has just started! \n")
        print("Your total score is:", player_scores[player_idx],"\n")
        current_score=0 #This set the score for the current round 
        while True:
        #Asking the player to press y(small letter)
            should_roll = input("Would you like to roll (y)?")
            if should_roll.lower() != "y":
                break
            
            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a:", value)
            print("Your score is:", current_score) 

        player_scores[player_idx] += current_score #This adds the current score to their Total score
        print("Your total score is:", player_scores[player_idx])  

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)   #This finds the palce or index of the max score in the list

print("Player number", winning_idx + 1, "is the winner with a score of:", max_score)

