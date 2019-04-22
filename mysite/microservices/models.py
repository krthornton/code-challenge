from django.db import models


# class for a player model
class Player(models.Model):
    pid = models.IntegerField(unique=True, primary_key=True)
    pname = models.CharField(max_length=20)

    # return the player's ID, name, and score as one string
    def __str__(self):
        retval = "%s %s" % (self.pid, self.pname)
        return retval


# class for a battleroom model
class Battleroom(models.Model):
    bid = models.IntegerField(unique=True, primary_key=True)
    bname = models.CharField(max_length=50)

    def __str__(self):
        retval = "%s" % (self.bname)
        return retval


# class for a relationship between a battleroom and a player
class Score(models.Model):
    score = models.IntegerField(default=0)
    battleroom = models.ForeignKey(Battleroom, on_delete=models.SET_NULL, null=True)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    rank = models.IntegerField(default=0)

    def __str__(self):
        retval = "%s %s %s" % (self.battleroom, self.player, self.score)
        return retval

    class Meta:
        unique_together = ("battleroom", "player")
