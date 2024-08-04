from . import Move
from .user import user_strategy
from strategy import Strategy


def move_victory(move_one: Move, move_two: Move) -> tuple[bool, bool]:
    """
    Calculates if the players playing the corresponding moves win or lose.
    
    Paramters
    ---------
    move_one : Move
        Move played by the first player (semantically first).
    move_two : Move
        Move played by the second player (semantically second).
    
    Returns
    -------
    tuple[bool, bool]
        A tuple containing win or loss status of the players (semantically ordered to the first and second player respectively).
        True represents a definite win, only one player can be the winner.
        False represents a loss, if the other player has won.
        A tuple with only False values denotes a draw.
    """
    
    if move_one == move_two:
        return (False, False)
    match (move_one):
        case Move.ROCK:
            return (True, False) if move_two == Move.SCISSORS else (False, True)
        case Move.PAPER:
            return (True, False) if move_two == Move.ROCK else (False, True)
        case Move.SCISSORS:
            return (True, False) if move_two == Move.PAPER else (False, True)


def play_game_cli(strategy: Strategy = Strategy.RANDOM) -> None:
    """
    Runs the game simulation on cli waiting for user input and running the computer selected strategy.
    The result of the game simulation will be printed on CLI.
    
    Parameters
    ----------
    strategy: Strategy
        The strategy that the computer player will run (defaults to Strategy.Random)
    """
    
    user_move = user_strategy()
    computer_strategy = strategy.get_strategy()
    computer_move = computer_strategy()
    user_wins, computer_wins = move_victory(user_move, computer_move)
    print(f"User played {user_move}, computer played {computer_move}")
    if user_wins:
        print("User WON this round!")
    elif computer_wins:
        print("Computer WON this round!")
    else:
        print("Round ends in a draw")
    print()