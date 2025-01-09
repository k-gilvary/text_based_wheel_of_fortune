import random

# List of categories and answers
QUESTIONS = [
    {"category": "Around the House", "answers": [
        "A Glass Of Bourbon"
    ]}
]

# main function
def main():
    play_game()

# game function
def play_game():
    # prompt user to play game and amt of players
    print("Welcome to Wheel Of Fortune!")
    num_players = input("How many players? (Type 1, 2, or 3): ")

    # display question, player, money, and options (spin, solve, buy vowel)
    print("\n_  _ _ _ _ _  _ _  _ _ _ _ _ _ _\n\n")
    print(f"The category is: {QUESTIONS[0]["category"]}\n\n")
    print("How much you have this round: $4000")
    print("Current winnings: $1234")
    player_choice = input("What would you like to do? (1: Spin, 2: Solve, 3: Buy Vowel): ")

main()
