from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from microservices.models import get_player, Player

import json


# main index
@csrf_exempt
def index(request):
    # check if this is a put request
    if request.method == "POST":
        # attempt to parse the given JSON
        try:
            # parse the body as JSON
            parsed = json.loads(request.body)

            # if given, fetch player by pid
            player = None
            players = None
            if "pid" in parsed["Player"]:
                player = get_player(pid=parsed["Player"]["pid"])
            # else, fetch player by player name
            elif "pname" in parsed["Player"]:
                print("DEBUG: searching by pname")
                players = get_player(pname=parsed["Player"]["pname"])
                print("DEBUG", players)

            # define an empty dict to fill with player information
            response_dict = {"Players": {}}

            # got a player by PID
            if player is not None:
                response_dict["Players"] = {player.pname: {"Score": player.get_score()}}
                response_data = json.dumps(response_dict)
                return JsonResponse(response_data, content_type="application/json", safe=False)

            # got a list of players by pname
            elif players is not None:
                # return info about each player that has this pname
                for p in players:
                    response_dict["Players"][p.pname] = {"Score": p.get_score()}
                response_data = json.dumps(response_dict)
                return JsonResponse(response_data, content_type="application/json", safe=False)

        except json.JSONDecodeError:
            # failed to parse the request body as JSON
            error = "Failed to parse POST data as json.\n"
            error += str(request.body)
            return HttpResponse(error)

        except TypeError as e:
            if str(e) == "string indices must be integers":
                # json was parsed fine but it was not in the expected format
                error = "Improperly formatted JSON.\n"
                error += str(request.body)
                return HttpResponse(error)

        except KeyError as e:
            if str(e) == "'Player'":
                # json was parsed fine but it did not find the expected Player field
                error = "\"Player\" key not found in POST data\n"
                error += str(request.body)
                return HttpResponse(error)

        except Player.DoesNotExist as e:
            # could not find the player that was requested
            error = "No player by the pid \"" + parsed["Player"]["pid"] + "\" was found."
            return HttpResponse(error)

    # if all else fails, return a basic HTTP page
    return HttpResponse("Something didn't work...")
