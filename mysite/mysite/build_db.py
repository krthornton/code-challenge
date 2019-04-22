import django
django.setup()  # must run setup before importing anything else

from microservices.models import *


pat = Player.objects.create(pid=1, pname="Patricia")
mary = Player.objects.create(pid=2, pname="Mary")
james = Player.objects.create(pid=3, pname="James")
jenn = Player.objects.create(pid=4, pname="Jennifer")
john = Player.objects.create(pid=5, pname="John")
rob = Player.objects.create(pid=6, pname="Robert")

broom_one = Battleroom.objects.create(bid=1, bname="one")
broom_thirty = Battleroom.objects.create(bid=30, bname="thirty")

john_broom_one = Score.objects.create(player_id=5, battleroom_id=1, score=500, rank=1)
pat_broom_one = Score.objects.create(player_id=1, battleroom_id=1, score=450, rank=3)
mary_broom_one = Score.objects.create(player_id=2, battleroom_id=1, score=300, rank=5)
james_broom_one = Score.objects.create(player_id=3, battleroom_id=1, score=375, rank=4)
jenn_broom_one = Score.objects.create(player_id=4, battleroom_id=1, score=225, rank=6)
rob_broom_one = Score.objects.create(player_id=6, battleroom_id=1, score=460, rank=2)

john_broom_thirty = Score.objects.create(player_id=5, battleroom_id=30, score=200, rank=5)
pat_broom_thirty = Score.objects.create(player_id=1, battleroom_id=30, score=150, rank=6)
mary_broom_thirty = Score.objects.create(player_id=2, battleroom_id=30, score=300, rank=1)
james_broom_thirty = Score.objects.create(player_id=3, battleroom_id=30, score=275, rank=2)
jenn_broom_thirty = Score.objects.create(player_id=4, battleroom_id=30, score=225, rank=4)
rob_broom_thirty = Score.objects.create(player_id=6, battleroom_id=30, score=260, rank=3)
