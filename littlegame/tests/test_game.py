import unittest

from littlegame.game import Move
from littlegame.game.gameplay import move_victory


class TestGameplay(unittest.TestCase):

    def test_move_victory_draw(self):
        win1, win2 = move_victory(Move.ROCK, Move.ROCK)
        self.assertFalse(win1)
        self.assertFalse(win2)
        win1, win2 = move_victory(Move.PAPER, Move.PAPER)
        self.assertFalse(win1)
        self.assertFalse(win2)
        win1, win2 = move_victory(Move.SCISSORS, Move.SCISSORS)
        self.assertFalse(win1)
        self.assertFalse(win2)

    def test_move_victory_player1_wins(self):
        win1, win2 = move_victory(Move.ROCK, Move.SCISSORS)
        self.assertTrue(win1)
        self.assertFalse(win2)
        win1, win2 = move_victory(Move.PAPER, Move.ROCK)
        self.assertTrue(win1)
        self.assertFalse(win2)
        win1, win2 = move_victory(Move.SCISSORS, Move.PAPER)
        self.assertTrue(win1)
        self.assertFalse(win2)
    
    def test_move_victory_player2_wins(self):
        win1, win2 = move_victory(Move.SCISSORS, Move.ROCK)
        self.assertFalse(win1)
        self.assertTrue(win2)
        win1, win2 = move_victory(Move.ROCK, Move.PAPER)
        self.assertFalse(win1)
        self.assertTrue(win2)
        win1, win2 = move_victory(Move.PAPER, Move.SCISSORS)
        self.assertFalse(win1)
        self.assertTrue(win2)


if __name__ == '__main__':
    unittest.main()