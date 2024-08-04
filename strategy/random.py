import random

from game import Move, ALL_MOVES


def random_move() -> Move:
    return random.choice(ALL_MOVES)


__all__ = [random_move]