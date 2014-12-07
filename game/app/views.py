from django.shortcuts import render_to_response
from game.app.models import CurrentStatus
from django.http import HttpResponse
import json


def new_game(request):
    #CurrentStatus.restart_game()
    return render_to_response('new_game.html')


def game(request, player_id):
    return render_to_response('game.html', {"player_id": int(player_id)})


def game(request, player_id):
    return render_to_response('game.html', {"player_id": int(player_id)})


def get_current_state(request):
    data = CurrentStatus.to_dict()
    return HttpResponse(json.dumps(data), content_type="application/json")