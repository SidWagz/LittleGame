from game import Move


def rock_move() -> Move:
    return Move.ROCK


def paper_move() -> Move:
    return Move.PAPER


def scissors_move() -> Move:
    return Move.SCISSORS


def single_move_facade(move_name: str) -> Move:
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