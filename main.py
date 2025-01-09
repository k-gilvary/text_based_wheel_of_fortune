import random, time

# List of categories and answers
QUESTIONS = [
    {"category": "Around the House", "answers": [
        "A  G l a s s  O f  B o u r b o n"
    ]}
]
VOWEL_PRICE = 250
WHEEL = [700, "Lose A Turn", 800, 500, 650, 500, 900, "Bankrupt", 5000, 500, 600, 700, 600, 650, 500, 700, 500, 600, 550, 500, 600, "Bankrupt", 650]

# main function
def main():
    play_game()

# spin function
def spin():
    print("Spinning . . .")
    time.sleep(1)
    return WHEEL[random.randint(0, 23)]

# handle guess function
def handle_guess(letter, full_answer, current_ans):
    found = False
    curr_ans_list = list(current_ans)
    full_ans_list = list(full_answer)

    # print(curr_ans_list, full_ans_list)

    for c in range(0, len(full_ans_list)):
        if full_ans_list[c].upper() == letter.upper():
            curr_ans_list[c] = letter
            print(curr_ans_list)
            found = True
    
    return(''.join(curr_ans_list), found)

# game function
def play_game():
    # prompt user to play game and amt of players
    print("Welcome to Wheel Of Fortune!")
    num_players = input("How many players? (Type 1, 2, or 3): ")

    # display question, player, money, and options (spin, solve, buy vowel)
    current_shown_answer = "\n_  _ _ _ _ _  _ _  _ _ _ _ _ _ _\n\n"
    print(current_shown_answer)
    print(f"The category is: {QUESTIONS[0]["category"]}\n\n")
    print("How much you have this round: $4000")
    print("Current winnings: $1234")
    player_choice = input("What would you like to do? (1: Spin, 2: Solve, 3: Buy Vowel): ")

    # spin
    wheel_spin = spin()
    guessed_letter = input(f"${wheel_spin}! Guess a letter: ")

    #handle guess
    current_shown_answer, found = handle_guess(guessed_letter, " A  G l a s s  O f  B o u r b o n", current_shown_answer)
    print(current_shown_answer, found)

main()
