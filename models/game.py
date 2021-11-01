class Game():
    def __init__(self,player1,player2): 
        self.player1 = player1
        self.player2 = player2
       
    def run (self):
        if self.player1.choice==self.player2.choice:
            return None
        if self.player1.choice=="rock" and self.player2.choice=="scissors":
            return "Player 1 wins by playing rock"
        if self.player1.choice=="rock" and self.player2.choice=="paper":
            return "Player 2 wins by playing paper"   
        if self.player1.choice=="scissors" and self.player2.choice=="rock":
            return "Player 2 wins by playing rock"  
        if self.player1.choice=="scissors" and self.player2.choice=="paper":
            return "Player 1 wins by playing scissors"  
        if self.player1.choice=="paper" and self.player2.choice=="rock":
            return "Player 1 wins by playing paper"  
        if self.player1.choice=="paper" and self.player2.choice=="scissors":
            return "Player 2 wins by playing scissors"        


