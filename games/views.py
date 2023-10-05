from django.views.generic import TemplateView

import json
from django.http import JsonResponse
from games.models import GameScore


class AnagramHuntView(TemplateView):
    template_name = "games/anagram-hunt.html"


class MathFactsView(TemplateView):
    template_name = "games/math-facts.html"


class MathFactsPlayView(MathFactsView):
    template_name = "games/math-facts-play.html"


def record_score(request):
    data = json.loads(request.body)

    user_name = data["user-name"]
    game = data["game"]
    score = data["score"]

    new_score = GameScore(user_name=user_name, game=game, score=score)
    new_score.save()

    response = {"success": True}

    return JsonResponse(response)
