from django.db import models

# Create your models here.
from django.db import models

class CurrentStatus(models.Model):
    row = models.SmallIntegerField()
    col = models.SmallIntegerField()
    value = models.BooleanField(default=False)
    player_id = models.IntegerField(null=True, blank=True)

    @classmethod
    def restart_game(cls):
        CurrentStatus.objects.all().delete()
        for r in xrange(6):
            for c in xrange(7):
                current_status = CurrentStatus(row=r, col=c)
                current_status.save()

