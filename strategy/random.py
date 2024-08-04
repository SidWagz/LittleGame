import random

from game import Move, ALL_MOVES


def random_move() -> Move:
    """
    Provides a random legal move from all the available legal move set.
    
    Returns
    -------
    Move
        A random legal move.
    """
    
    return random.choice(ALL_MOVES)

__all__ = [random_move]