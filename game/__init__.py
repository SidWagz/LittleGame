from enum import Enum


class Move(Enum):
    ROCK = "Rock"
    PAPER = "Paper"
    SCISSORS = "Scissors"
    
    
    def __repr__(self):
        return self.value
    
    
    def __str__(self):
        return repr(self)


ALL_MOVES = list(Move)


__all__ = [Move]