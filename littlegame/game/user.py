from . import Move, ALL_MOVES


QUIT_COUNTER_MAX = 3


def _user_input() -> str:
    """
    Takes the user input from CLI.
    
    Returns
    -------
    str
        The string value typed by user on the CLI
    """
    
    user_choice = input(f"Choose from {ALL_MOVES}: ")
    return user_choice
    

def user_strategy() -> Move:
    """
    Takes the user input from CLI and checks if it is a legal move.
    In the case it is a legal move, the move is passed on.
    In case of an illegal input, the CLI tries upto 3 times for a legal input before terminating the application.
    
    Optionally, the user can input numerical values representing the positonal value of the move in the user prompt, starting from 1.
    
    Returns
    -------
    Move
        The move that the user selected.
    
    Raises
    ------
    ValueError
        If the user enters too many illegal move inputs for a single try.
    """
    
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
        raise ValueError("Quiting application as you have entered too many illegal move")
    return Move(user_choice)