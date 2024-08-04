from enum import Enum
from itertools import cycle, islice, repeat

from game.gameplay import play_game
from strategy import Strategy, ALL_STRATEGIES


def play_games(no_of_games: int, strategies: list[Strategy] = None) -> None:
    if not strategies:
        strategies = repeat(Strategy.RANDOM, no_of_games)
    else:
        strategies = islice(cycle(strategies), 0, no_of_games)
    for strategy in strategies:
        play_game(strategy)


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