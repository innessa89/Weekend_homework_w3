import unittest
from models.player import Player
from models.game import Game


class TestGame(unittest.TestCase):

    def setUp(self):
        self.player_1=Player("Player_1","rock")
        self.player_2=Player("Player_2","rock")
        self.player_3=Player("Player_1","scissors")
        self.player_4=Player("Player_2","scissors")
        self.player_5=Player("Player_1","paper")
        self.player_6=Player("Player_2","paper")

    def test_resul_of_game_none(self):
        gameReturn=Game(self.player_1,self.player_2).run()
        self.assertEqual(None,gameReturn)

    def test_resulf_of_game_player1(self):
        gameReturn1=Game(self.player_1,self.player_4).run()
        gameReturn2=Game(self.player_1,self.player_6).run()  
        gameReturn3=Game(self.player_3,self.player_2).run()  
        gameReturn4=Game(self.player_3,self.player_6).run()
        gameReturn5=Game(self.player_5,self.player_2).run()
        gameReturn6=Game(self.player_5,self.player_4).run()
        self.assertEqual("Player 1 wins by playing rock",gameReturn1)
        self.assertEqual("Player 2 wins by playing paper",gameReturn2)
        self.assertEqual("Player 2 wins by playing rock",gameReturn3)
        self.assertEqual("Player 1 wins by playing scissors",gameReturn4)
        self.assertEqual("Player 1 wins by playing paper",gameReturn5)
        self.assertEqual("Player 2 wins by playing scissors",gameReturn6)