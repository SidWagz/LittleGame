from enum import Enum

from game import Move
from .random import random_move
from .singlemove import single_move_facade


class Strategy(Enum):
    """A class to keep track of the only legal strategies implemented in the game"""
    
    ROCK_MOVE = "Rock" # Plays only rock move
    PAPER_MOVE = "Paper" # Plays only paper move
    SCISSORS_MOVE = "Scissors" # Plays only scissors move
    RANDOM = "Random" # Plays a random legal move        
    
    def __repr__(self):
        return self.value    
    
    def __str__(self):
        return repr(self)    
    
    def get_strategy(self) -> callable[[], Move]:
        """
        This give back a callable that calculates and returns a legal move as per the strategy it represents.
        
        Returns
        -------
        callable[[], Move]
            The strategy function that produces a single legal move for the calling strategy for a call.
            
        Raises
        ------
        NotImplementedError
            If the selected strategy is in this enum directory but the underlying move callable is not yet implemented.
        """
        
        match(self):
            case Strategy.ROCK_MOVE | Strategy.PAPER_MOVE | Strategy.SCISSORS_MOVE:
                return single_move_facade(self.value)
            case Strategy.RANDOM:
                return random_move
            case _:
                raise NotImplementedError(f"The selected strategy {self} has been fully implemented")

ALL_STRATEGIES = list(Strategy)

__all__ = [
    Strategy,
    ALL_STRATEGIES
]