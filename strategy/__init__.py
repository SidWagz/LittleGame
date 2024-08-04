from enum import Enum

from .random import random_move


class Strategy(Enum):
    RANDOM = "Random"
        
    
    def __repr__(self):
        return self.value
    
    
    def __str__(self):
        return repr(self)
    
    
    def get_strategy(self):
        match(self):
            case Strategy.RANDOM:
                return random_move

ALL_STRATEGIES = list(Strategy)


__all__ = [
    Strategy,
    ALL_STRATEGIES
]