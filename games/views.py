from django.views.generic import ListView, TemplateView

import json
from django.http import JsonResponse
from games.models import GameScore


class AnagramHuntView(TemplateView):
    template_name = "games/anagram-hunt.html"


class GameScoreView(ListView):
    model = GameScore
    template_name = "games/game-scores.html"

    def get_context_data(self, **kwargs):
        context = super(GameScoreView, self).get_context_data(**kwargs)
        context["anagram_scores"] = GameScore.objects.filter(
            game__exact="ANAGRAM"
        ).order_by("-score")
        context["math_scores"] = GameScore.objects.filter(game__exact="MATH").order_by(
            "-score"
        )
        return context


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
