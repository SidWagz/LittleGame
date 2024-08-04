from game import Move


def rock_move() -> Move:
    """
    Provides a legal move to represent rock.
    
    Returns
    -------
    Move
        The rock move.
    """
    
    return Move.ROCK


def paper_move() -> Move:
    """
    Provides a legal move to represent paper.
    
    Returns
    -------
    Move
        The paper move.
    """
    
    return Move.PAPER


def scissors_move() -> Move:
    """
    Provides a legal move to represent scissors.
    
    Returns
    -------
    Move
        The scissor move.
    """
    
    return Move.SCISSORS


def single_move_facade(move_name: str) -> callable[[str], Move]:
    """
    Factory method that provides the corresponding move generator.
    
    Parameter
    ---------
    move_name : str
        The value of the move to create the factory for, with choices ["Rock", "Paper", "Scissors"].
    
    Returns
    -------
    callable[[str], Move]
        A move strategy callable corresponding to the function parameter.
        
    Raises
    ------
    ValueError
        If the move_name parameter passed contains any string other than the allowed choices.
    """
    
    match(move_name):
        case "Rock":
            return rock_move
        case "Paper":
            return paper_move
        case "Scissors":
            return scissors_move
        case _:
            raise ValueError(f"Unexpected illegal move name {move_name}")


__all__ = [
    rock_move,
    paper_move,
    scissors_move,
    single_move_facade
]