import unittest

from littlegame.game import Move, ALL_MOVES
from littlegame.strategy.random import random_move
from littlegame.strategy.singlemove import rock_move, paper_move, scissors_move, single_move_facade
from littlegame.strategy.vengence import VengenceStrategy


class TestSingleMoveStrategy(unittest.TestCase):

    def test_rock_move(self):
        move = rock_move()
        self.assertEqual(move, Move.ROCK)
        same_move = rock_move()
        self.assertEqual(same_move, Move.ROCK)
    

    def test_paper_move(self):
        move = paper_move()
        self.assertEqual(move, Move.PAPER)
        same_move = paper_move()
        self.assertEqual(same_move, Move.PAPER)
    
    
    def test_scissors_move(self):
        move = scissors_move()
        self.assertEqual(move, Move.SCISSORS)
        same_move = scissors_move()
        self.assertEqual(same_move, Move.SCISSORS)
    
    
    def test_single_move_facade(self):
        move = single_move_facade("Rock")()
        self.assertEqual(move, Move.ROCK)        
        second_move = single_move_facade("Paper")()
        self.assertEqual(second_move, Move.PAPER)        
        third_move = single_move_facade("Scissors")()
        self.assertEqual(third_move, Move.SCISSORS)
        with self.assertRaises(ValueError):
            single_move_facade("AnyOtherString")


class TestRandomStrategy(unittest.TestCase):

    def test_randome_move(self):
        move = random_move()
        self.assertIn(move, ALL_MOVES)
        new_move = random_move()
        self.assertIn(new_move, ALL_MOVES)
        new_move = random_move()
        self.assertIn(new_move, ALL_MOVES)


class TestVengenceStrategy(unittest.TestCase):

    def test_vengence_move(self):
        strategy = VengenceStrategy()
        counter_moves = { 
            Move.ROCK: Move.SCISSORS,
            Move.SCISSORS: Move.PAPER,
            Move.PAPER: Move.ROCK
        }
        move = strategy()
        self.assertIn(move, ALL_MOVES)
        strategy.push_feedback(False)
        new_move = strategy()
        self.assertEqual(new_move, counter_moves[move]) 


if __name__ == '__main__':
    unittest.main()