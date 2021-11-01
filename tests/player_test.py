import unittest
from models.player import Player

class TestPlayer(unittest.TestCase):
    
    def setUp(self):
        self.player_1 = Player("Player_1", "rock")
        self.player_2= Player("Player_2", "scissors")

    def test_player_has_name(self):
        self.assertEqual("Player_1",self.player_1.name)

    def test_player_has_choise(self):
        self.assertEqual("rock",self.player_1.choice)
  

        