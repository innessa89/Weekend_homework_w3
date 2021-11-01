from flask import render_template, request
from app import app
from models.player import Player
from models.game_result import add_user_and_choice, players
from models.game import Game

@app.route('/')
def start_page():
    return render_template("start_page.html", title ='Start Game')
  
    
@app.route('/start')
def index():
    return render_template('index.html',title='Game') 
   

@app.route('/start', methods=["POST"])
def play_game():
    player1_choice = request.form["player_one_choice"]
    player2_choice= request.form["player_two_choice"]
    player1 = Player("player1", player1_choice)
    player2 = Player("player2", player2_choice)
    result = Game(player1, player2).run()
    return render_template('index.html',title='Game', result = result)

@app.route('/user')
def list_of_players():
   
    return render_template('user.html',title='Game', players = players)    

