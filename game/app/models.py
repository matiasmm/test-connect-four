from django.db import models


class TableStatus(models.Model):
    row = models.SmallIntegerField()
    col = models.SmallIntegerField()
    player_id = models.IntegerField(null=True, blank=True)

    @classmethod
    def restart_game(cls):
        cls.objects.all().delete()
        for r in xrange(6):
            for c in xrange(7):
                current_status = cls(row=r, col=c)
                current_status.save()


    @classmethod
    def to_dict(cls):
        r = [[None]*7 for x in xrange(6)]
        for cs in cls.objects.all():
            r[cs.row][cs.col] = cs.player_id
        return r


class GameStatus(models.Model):
    turn = models.SmallIntegerField(null=True, blank=True)
    # either null or the id of the player who won
    ended = models.SmallIntegerField(null=True, blank=True)


    @classmethod
    def restart_game(cls):
        cls.objects.all().delete()
        game = cls(turn=1)
        game.save()

        TableStatus.restart_game()


    @classmethod
    def to_dict(cls):
        game = cls.objects.first()
        r = dict(table=TableStatus.to_dict(), turn=game.turn , ended=game.ended)
        return r
