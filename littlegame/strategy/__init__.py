from abc import abstractmethod
from enum import Enum
from typing import Callable, Union

from ..game import Move
from .base import StatefulStrategy
from .random import random_move
from .singlemove import single_move_facade
from .vengence import VengenceStrategy


class Strategy(Enum):
    """A class to keep track of the only legal strategies implemented in the game"""
    
    """Stateless strategies"""
    ROCK_MOVE = "Rock" # Plays only rock move
    PAPER_MOVE = "Paper" # Plays only paper move
    SCISSORS_MOVE = "Scissors" # Plays only scissors move
    RANDOM = "Random" # Plays a random legal move       
    
    """Stateful strategies"""
    VENGENCE = "Vengence" # If the last move generated a loss, the next move will be the counter move for the losing move. For a win or the first move, it plays random.
        
    def __repr__(self):
        return self.value    
    
    def __str__(self):
        return repr(self)
    
    @property
    def runner(self) -> Callable[[], Move]:
        """
        Returns the strategy callable (statefull or stateless) that is set.
        """
        return get_strategy_runner(self)
    
    def feedback(self, win: bool) -> None:
        """
        A feedback hook that can be used to keep track of the last played move generated a win or a loss
        """
        
        if self.runner and isinstance(self.runner, StatefulStrategy):
            self.runner.push_feedback(win)


_CACHED_RUNNERS = {
    Strategy.VENGENCE: VengenceStrategy()
}

def get_strategy_runner(strategy: Strategy) -> Callable[[], Move]:
    """
    This give back a callable that calculates and returns a legal move as per the strategy it represents.
        
    Parameters
    ----------
    strategy : Strategy
        The strategy against which the move generator is to be returned
        
    Returns
    -------
    Callable[[], Move]
        The strategy function that produces a single legal move for the calling strategy for a call.
            
    Raises
    ------
    NotImplementedError
        If the selected strategy is in this enum directory but the underlying move callable is not yet implemented.
    """
        
    match(strategy):
        case Strategy.ROCK_MOVE | Strategy.PAPER_MOVE | Strategy.SCISSORS_MOVE:
            return single_move_facade(strategy.value)
        case Strategy.RANDOM:
            return random_move
        case Strategy.VENGENCE:
            return _CACHED_RUNNERS[Strategy.VENGENCE]
        case _:
            raise NotImplementedError(f"The selected strategy {strategy} has been fully implemented")
    
        
ALL_STRATEGIES = list(Strategy)

__all__ = [
    Strategy,
    StatefulStrategy,
    ALL_STRATEGIES
]