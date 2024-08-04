from . import Move, ALL_MOVES


QUIT_COUNTER_MAX = 3


def _user_input() -> str:
    user_choice = input(f"Choose from {ALL_MOVES}: ")
    return user_choice
    

def user_strategy() -> Move:
    user_choice = _user_input()
    quit_counter = 0
    while (quit_counter := quit_counter+1) < QUIT_COUNTER_MAX:
        if user_choice in ALL_MOVES:
            break
        if user_choice.isdigit() and 1 <= int(user_choice) <= len(ALL_MOVES):
            user_choice = ALL_MOVES[int(user_choice)-1]
            break
        print("The choice you entered does not seem to be a legal move\nTry again\n")
        user_choice = _user_input()
    else:
        print("\nQuiting application as you have entered too many illegal move")
        import sys
        sys.exit(0)
    return Move(user_choice)