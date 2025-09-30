import random
import rps_functions

def main():
    player_win_count = 0
    computerWinCount = 0


    print("Welcome top rock paper scissors game!")

    winning_score = 2
    while player_win_count < winning_score and computerWinCount < winning_score:

        player_input = rps_functions.get_user_input()
        com_turn = rps_functions.get_computer_choice()

        print("The computer went: " + com_turn)

        player_outcome = rps_functions.get_outcome(player_input,com_turn)

        if player_outcome == "w":
            print("You won this round!")
            player_win_count+=1
        elif player_outcome == "d":
            print("It's a draw!")
        else:
            print("You lost this round!")
            computerWinCount+=1

    if player_win_count == winning_score:
        print("You Won!!!!!")
    else:
        print("Computer Won!")

if __name__ == "__main__":
    main()