from enum import Enum

from .random import random_move
from .singlemove import single_move_facade


class Strategy(Enum):
    ROCK_MOVE = "Rock"
    PAPER_MOVE = "Paper"
    SCISSORS_MOVE = "Scissors"
    RANDOM = "Random"
        
    
    def __repr__(self):
        return self.value
    
    
    def __str__(self):
        return repr(self)
    
    
    def get_strategy(self):
        match(self):
            case Strategy.ROCK_MOVE | Strategy.PAPER_MOVE | Strategy.SCISSORS_MOVE:
                return single_move_facade(self.value)
            case Strategy.RANDOM:
                return random_move

ALL_STRATEGIES = list(Strategy)


__all__ = [
    Strategy,
    ALL_STRATEGIES
]