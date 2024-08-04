from . import Move
from .user import user_strategy
from strategy import Strategy


def move_victory(move_one: Move, move_two: Move) -> tuple[bool, bool]:
    if move_one == move_two:
        return (False, False)
    match (move_one):
        case Move.ROCK:
            return (True, False) if move_two == Move.SCISSORS else (False, True)
        case Move.PAPER:
            return (True, False) if move_two == Move.ROCK else (False, True)
        case Move.SCISSORS:
            return (True, False) if move_two == Move.PAPER else (False, True)


def play_game(strategy: Strategy = Strategy.RANDOM) -> None:
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