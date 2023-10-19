from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView, DetailView, ListView, TemplateView

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

        # Anagram Hunt context
        context["anagram_settings"] = GameScore.objects.filter(
            game__exact="ANAGRAM"
        ).values("word_length", "total_words")
        context["anagram_scores"] = GameScore.objects.filter(
            game__exact="ANAGRAM"
        ).order_by("-score")

        # Math Facts Practice context
        context["math_settings"] = GameScore.objects.filter(game__exact="MATH").values(
            "operation", "max_number"
        )
        context["math_scores"] = GameScore.objects.filter(game__exact="MATH").order_by(
            "-score"
        )

        return context


class GameScoreDeleteView(UserPassesTestMixin, DeleteView):
    model = GameScore
    success_url = reverse_lazy("games:game-scores")

    def delete(self, request, *args, **kwargs):
        result = super().delete(request, *args, **kwargs)
        return result

    def form_valid(self, form):
        messages.success(self.request, "Score deleted")
        return super().form_valid(form)

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.user


class GameScoreDetailView(LoginRequiredMixin, DetailView):
    model = GameScore
    template_name = "games/game-score-detail.html"


class MathFactsView(TemplateView):
    template_name = "games/math-facts.html"


class MathFactsPlayView(MathFactsView):
    template_name = "games/math-facts-play.html"


@login_required
def record_score(request):
    data = json.loads(request.body)

    user = request.user
    game = data["game"]
    score = data["score"]

    new_score = GameScore(user=user, game=game, score=score)
    new_score.save()

    response = {"success": True}

    return JsonResponse(response)
