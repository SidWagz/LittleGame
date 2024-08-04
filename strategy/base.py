from abc import abstractmethod
import warnings

from game import Move


class StatefulStrategy:
    """A base class for every stateful strategy"""
    
    def __init__(self):
        """Initialize th einternal state queue"""
        
        self.moves = []
        self.wins = []
        self.last_move = None
        
    def push_feedback(self, win: bool) -> None:
        """
        Set the last_move that was played and the corresponding feedback win/lose into the internal state queue.
        """
        
        if self.last_move is None:
            warnings.warn("Cannot accept the win/lose feeedback as there was no last move played")
            return
        self.moves.append(self.last_move)
        self.wins.append(win)
        self.last_move = None
    
    @abstractmethod
    def next_move(self) -> Move:
        pass
    
    def __call__(self) -> Move:
        """Callable that directly plays the next move for the child strategy"""
        
        self.last_move = self.next_move()
        return self.last_move