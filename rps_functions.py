import random

def get_user_input():
    p_input = ""
    is_valid_input = False
    while not is_valid_input:
        p_input = input("It's your turn! r/p/s \n")
        if p_input != "s" and p_input != "p" and p_input != "r":
            print("You must enter r, p or s!")
        else:
            is_valid_input = True
    return p_input

def get_computer_choice():
    comchoices = {0: "r", 1: "p", 2: "s"}
    comturn = comchoices[random.randint(0, 2)]
    return comturn


def get_outcome(player_input,com_turn):
    # Compares Player and Computer choices
    round = player_input + com_turn
    player_results = {
        "rr": "d", "rp": "l", "rs": "w",
        "pp": "d", "pr": "w", "ps": "l",
        "ss": "d", "sr": "l", "sp": "w"
        }
    player_outcome = player_results[round]
    return player_outcome