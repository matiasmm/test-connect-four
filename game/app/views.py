import json

from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from game.app.models import TableStatus, GameStatus


def new_game(request):
    GameStatus.restart_game()
    return render_to_response('new_game.html')


def game(request, player_id):
    return render_to_response('game.html', {"player_id": int(player_id)})


def get_current_state(request):
    data = GameStatus.to_dict()
    return HttpResponse(json.dumps(data), content_type="application/json")


def is_ended(row, col):
    table = TableStatus.to_dict()

    directions = ((1,1),(-1,-1),(1,-1),(-1,1),(0,1),(1,0),(0,1),(1,0),)
    for dr, dc in directions:
        curr_row = row
        curr_col = col

        pl = None
        count = 0

        while 0 <= curr_row <= 5 and 0 <= curr_col <= 6:
            ts = table[curr_row][curr_col]
            if ts != pl:
                pl = ts
                count = 0
            count += 1

            if count == 4 and pl:
                return pl

            curr_row += dr
            curr_col += dc

@csrf_exempt
def update(request):
    player_id = int(request.POST['player_id'])
    row = int(request.POST['row'])
    col = int(request.POST['col'])

    celd = TableStatus.objects.get(row=row, col=col)
    celd.player_id = player_id
    celd.save()

    if player_id == 1:
        turn = 2
    else:
        turn = 1

    game = GameStatus.objects.get()
    game.turn = turn
    game.ended = is_ended(row, col)
    game.save()

    return HttpResponse(json.dumps({'success': True}), content_type="application/json")