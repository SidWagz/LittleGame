from enum import Enum


class Move(Enum):
    """A class to keep track of the only legal moves in the game"""
    
    ROCK = "Rock" # "Represents the rock move"
    PAPER = "Paper" # "Represents the paper move"
    SCISSORS = "Scissors" # "Represents the scissors move"
    
    def __repr__(self):
        return self.value    
    
    def __str__(self):
        return repr(self)

ALL_MOVES = list(Move)

__all__ = [Move]