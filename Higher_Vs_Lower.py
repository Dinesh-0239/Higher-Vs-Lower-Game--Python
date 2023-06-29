"""
Date:- Jun 29, 2023
Creator:- Dinesh Singh

In this game we have given description to celebraties and according to it we have to check whose follower count is more is we guessed it write game will continue and score will be exceed by 1.
The first occurance when we got wrong answer the game will end with the final score.

"""
#Import necessary plan
from random import choice
from game_data import data
from art import logo, vs
from clear_screen import clear_screen

def quiz_question():
    """Returns random index position of game data"""
    return choice(data)

def play_game():
    """Main function of the game"""
    is_game_over = False
    option_A = quiz_question()
    score = 0
    print(logo)

    while not is_game_over:
        option_B = option_A
        print(f"Compare A: {option_A['name']}, a {option_A['description']}, from {option_A['country']}")
        print(vs)
    
        #Preventing same comparision occurance 
        while option_A == option_B:
            option_B = quiz_question()
    
        print(f"Against= B: {option_B['name']}, a {option_B['description']}, from {option_B['country']}")

        #comparing whose follower count is more
        if option_A['follower_count'] > option_B['follower_count']:
            option_A = option_B
            answer = 'A'
        else:
            answer = 'B'
        choice = input("Who has more followers? Type 'A' or 'B': ").upper()
        clear_screen()
        
        # Checking wheter you are correct or not
        if choice == answer:
            score += 1
            print(logo)
            print(f"You're right! Current Score: {score}.")
        else:
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}.")
            is_game_over = True

play_game()