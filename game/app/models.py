from django.db import models

# Create your models here.
from django.db import models

class CurrentStatus(models.Model):
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
        r = []
        for cs in CurrentStatus.objects.all():
            r.append(dict(row=cs.row, col=cs.col, player_id=cs.player_id))
        return r

