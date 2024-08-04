from ..game import Move
from . import StatefulStrategy
from .random import random_move

class VengenceStrategy(StatefulStrategy):
    """
    This strategy will play play a counter maove to the last loss move in its history.
    Else it play a random move as first, or if the last move was a win.
    """
    
    def next_move(self) -> Move:
        """
        Next move for this strategy following the class description strategy.
        
        Returns
        -------
        Move
            The counter move.
        """
        
        if not self.moves or self.wins[-1]:
            return random_move()
        losing_move = self.moves[-1]
        match(losing_move):
            case Move.ROCK:
                return Move.SCISSORS
            case Move.PAPER:
                return Move.ROCK
            case Move.SCISSORS:
                return Move.PAPER
            