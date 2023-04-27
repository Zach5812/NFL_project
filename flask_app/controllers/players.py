from flask_app import app, render_template, redirect, request, session, flash, bcrypt
from flask_app.models.player import players
import requests

@app.route('/')
def dashboard():
    data = players
    return render_template('dashboard.html', data = data)


@app.route('/find_player')
def player():
    player_id = request.args['player_id']
    id = False
    the_player = False
    for player in players:
        if player['displayName'] == player_id:
            the_player = player
            id = player['id']
    data = requests.get(f"https://site.web.api.espn.com/apis/common/v3/sports/football/nfl/athletes/{id}/stats").json()
    return render_template('player.html', player_id = the_player, data = data)


@app.route('/find_players')
def two_players():
    player1 = request.args['player1']
    id1 = False
    id2 = False
    the_player1 = False
    the_player2 = False
    for player in players:
        if player['displayName'] == player1:
            the_player1 = player
            id1 = player['id']
    player2 = request.args['player2']
    for player in players:
        if player['displayName'] == player2:
            the_player2 = player
            id2 = player['id']
    data1 = requests.get(f"https://site.web.api.espn.com/apis/common/v3/sports/football/nfl/athletes/{id1}/stats").json()
    data2 = requests.get(f"https://site.web.api.espn.com/apis/common/v3/sports/football/nfl/athletes/{id2}/stats").json()
    return render_template('players.html', player1 = the_player1, player2 = the_player2, data1 = data1, data2 = data2)
