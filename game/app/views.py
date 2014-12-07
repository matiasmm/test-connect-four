from django.shortcuts import render_to_response
from game.app.models import CurrentStatus

def new_game(request):
    #CurrentStatus.restart_game()
    return render_to_response('new_game.html')

def game(request, player_id):
    id = int(player_id)
    return render_to_response('game.html')