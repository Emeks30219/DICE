import random

def roll():
    min_value = 1
    max_value = 6
    return random.randint(min_value, max_value)

while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2-4 players.")
    else:
        print("INVALID, TRY AGAIN!")

max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    for player_idx in range(players):
        print("\nPlayer number", player_idx + 1, "turn has just started!\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll? (y/n): ")

            if should_roll.lower() == "y":
                value = roll()
                if value == 1:
                    print("You rolled a 1! Turn over, no points added.")
                    current_score = 0
                    break                                # end this player's turn
                else:
                    current_score += value
                    print("You rolled a:", value)
                    print("Your current turn score is:", current_score)
            else:
                print("You chose to stop rolling.")
                break                                    # player banks their score

        player_scores[player_idx] += current_score      # ✅ fixed typos
        print("Your total score is:", player_scores[player_idx])

# Announce the winner
winning_score = max(player_scores)
winner = player_scores.index(winning_score) + 1
print(f"\nPlayer {winner} wins with a score of {winning_score}!")
