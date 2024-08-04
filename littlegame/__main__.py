from enum import Enum
from itertools import cycle, islice, repeat

from .game.gameplay import play_game_cli
from .strategy import Strategy, ALL_STRATEGIES


def play_games(no_of_games: int, strategies: list[Strategy] = None) -> None:
    """
    This runs all the match setups and prints the final score of the current setup.
    """
    
    if not strategies:
        strategies = repeat(Strategy.RANDOM, no_of_games)
    else:
        strategies = islice(cycle(strategies), 0, no_of_games)
    scores = []
    scores = [play_game_cli(strategy) for strategy in strategies]
    total_score = scores[0]
    for score in scores[1:]:
        total_score += score
    
    print("Final scores are:")
    for key, value in total_score.items():
        print(key, ":", value)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(
        prog='LittleGame',
        description='This is a demo game for a user-computer interactive fun game of "Rock, Paper, and Scissors"')
    parser.add_argument('--rounds', metavar='N', type=int, default=1, help='Number of rounds to play this game')
    parser.add_argument('--strategies', type=Strategy, choices=ALL_STRATEGIES, nargs='+', help='Strategy to use')
    args = parser.parse_args()
    
    print()
    play_games(args.rounds, args.strategies)