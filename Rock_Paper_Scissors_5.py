# Rock, Paper, Scissors 

import random


def want_to_play():
    option = input("Do you want to play Rock, Paper, Scissors? \n"
                   "Type 'yes' or 'no': ")          #ask user if they want to play game

    option = check_input(option)
    
def check_input(yes_or_no):                         #check if user entered yes or no, not case sens.
    while yes_or_no.lower()!= 'yes' and yes_or_no.lower() != 'no':
            yes_or_no = input("Please enter 'yes' or 'no': ")
                                                    #let user re-enter
    if yes_or_no.lower() == "yes":                  #if user entered yes, play game
        play_game()
        
    if yes_or_no.lower() == "no":
        print("End of game.")                       #else, end program here
        return "no"
def play_game():                                    #ask user to enter either R,P,S
    player_choice = input("Choose: Enter 'rock', 'paper', or 'scissors': ").lower()
    

    while player_choice != 'rock' and player_choice != 'paper' and player_choice != 'scissors':
        player_choice = input("You spelled something incorrectly, please re-enter your choice: ")
                                                    #check user entry, let user re-enter
    
    comp_choice = comp_generator()                  #computer generator chooses RPS

    find_winner(player_choice, comp_choice)         #go to find winner function with 2 args


def comp_generator():
    comp_gen = random.randint(1,3)                  #random int generator 1-3 inclusive

    if comp_gen == 1:                                   # 1 = rock
        print("I chose rock.")                          # 2 = paper
        return "rock"                                   # 3 = scissors
    elif comp_gen == 2:
        print("I chose paper.")                     # return computers choice
        return "paper"
    else:
        print("I chose scissors.")
        return "scissors"

def find_winner(player, comp):                              #finding winner of game of if tie
    winner = True
    if player == "rock" and comp == "paper":                # paper > rock
        print("Paper beats rock! I win!")                   # rock > scissors
    elif comp == "rock" and player == "paper":              # scissors > paper
        print("Paper beats rock! You win!")

    elif player == "paper" and comp == "scissors":
        print("Scissors beats paper! I win!")
    elif player == "scissors" and comp == "paper":
        print("Scissors beats paper! You win!")

    elif player == "scissors" and comp == "rock":
        print("Rock beats scissors! I win!")
    elif player == "rock" and comp == "scissors":
        print("Rock beats scissors! You win!")

    else:
        winner = False
        print("It's a tie! Rematch!")
        play_game()

    if winner != False:
        again = input("Do you want to play again? 'yes' or 'no': ")  # ask user if they want to play again
        again_ans = check_input(again)

        if again_ans == "no":
            sure = input("But.. Are you suuureeeee? Play Again? 'yes' or 'no': ")
            sure_ans = check_input(sure)
            return
        

def main():
    want_to_play()
    
main()
