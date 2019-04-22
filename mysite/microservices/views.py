from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from microservices.models import Player, Battleroom, Score

import json
import statistics


# view for querying rank from the DB
@csrf_exempt
def rank(request):
    # check if this is a put request
    if request.method == "POST":
        try:
            # parse the body as JSON
            parsed = json.loads(request.body)

            # fetch a player by PID
            if "player_id" in parsed:
                player = Player.objects.get(pid=parsed["player_id"])
            else:
                return HttpResponse("No player_id given in POST data.\n%s" % request.body)

            # fetch the battleroom by BID
            if "battleroom_id" in parsed:
                battleroom = Battleroom.objects.get(bid=parsed["battleroom_id"])
            else:
                return HttpResponse("No battleroom_id given in POST data.\n%s" % request.body)

            # get score objects from database that matches player and battleroom
            score = Score.objects.get(player=player, battleroom=battleroom)

            # return the player's score and rank
            if score is not None:
                response_dict = {str(score.player): {"Score": score.score, "Rank": score.rank}}
                response_data = json.dumps(response_dict)
                return JsonResponse(response_data, content_type="application/json", safe=False)

        # handle improperly formatted JSON
        except json.decoder.JSONDecodeError as e:
            return HttpResponse("Failed to parse JSON in POST data.\n" + str(request.body))

        # handle exception when a player does not exist
        except Player.DoesNotExist as e:
            return HttpResponse("Could not find player by pid \"" + parsed["player_id"] + "\"")

        # handle exception when a battleroom does not exist
        except Battleroom.DoesNotExist as e:
            return HttpResponse("Could not find battleroom by bid \"" + parsed["battleroom_id"] + "\"")

    # if all else fails, return a basic HTTP page
    return HttpResponse("Something didn't work...")


# view for querying rank from the DB
@csrf_exempt
def leaderboard(request):
    # check if this is a put request
    if request.method == "GET":
        try:
            # parse the body as JSON
            parsed = json.loads(request.body)

            # ensure there is a battleroom_id in the POST data
            if "battleroom_id" not in parsed:
                return HttpResponse("No battleroom_id given in POST data.\n%s" % request.body)

            # get score objects from database that match the given battleroom
            scores_query = Score.objects.filter(battleroom=parsed["battleroom_id"]).order_by("rank")
            if scores_query.count() == 0:
                # if the query returns nothing, then the battleroom has no players or does not exist
                return HttpResponse("Either the battleroom " + parsed["battleroom_id"] + " does not exist or it has no players.")

            # build leaderboard
            leaders = {}
            scores = []
            for i in scores_query:
                leaders[i.player.pid] = i.score
                scores.append(i.score)

            # return the player's score and rank
            if scores is not {}:
                response_dict = {"Leaderboard (pid/score)": leaders, "Median Score": str(statistics.median(scores))}
                response_data = json.dumps(response_dict)
                return JsonResponse(response_data, content_type="application/json", safe=False)

        # handle improperly formatted JSON
        except json.decoder.JSONDecodeError as e:
            return HttpResponse("Failed to parse JSON in POST data.\n" + str(request.body))

    # if all else fails, return a basic HTTP page
    return HttpResponse("Something didn't work...")
