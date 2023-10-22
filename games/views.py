from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import DeleteView, DetailView, ListView, TemplateView

import json
from django.http import JsonResponse
from games.models import GameScore


class AnagramHuntView(TemplateView):
    template_name = "games/anagram-hunt.html"


class LeaderBoardView(ListView):
    model = GameScore
    ordering = ["-score", "game", "-created"]
    paginate_by = 10
    context_object_name = "top_scores"


class MyScoresView(LoginRequiredMixin, ListView):
    model = GameScore
    template_name = "games/myscores_list.html"
    paginate_by = 10
    context_object_name = "my_scores"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["username"] = self.request.user.username
        return context

    def get_queryset(self):
        user = self.request.user
        qs = GameScore.objects.filter(user=user)
        ordering = ["-score", "-game", "-created"]
        return qs.order_by(*ordering)


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


class MathFactsView(TemplateView):
    template_name = "games/math-facts.html"


class MathFactsPlayView(MathFactsView):
    template_name = "games/mathfacts_play.html"


@login_required
def record_score(request):
    data = json.loads(request.body)

    user = request.user
    game = data["game"]
    score = data["score"]

    new_score_data = {
        "user": user,
        "game": game,
        "score": score,
    }

    if game == "ANAGRAM":
        new_score_data["word_length"] = data.get("word_length")
        new_score_data["total_words"] = data.get("total_words")
    elif game == "MATH":
        new_score_data["operation"] = data.get("operation")
        new_score_data["max_number"] = data.get("max_number")

    new_score = GameScore(**new_score_data)
    new_score.save()

    response = {"success": True}

    return JsonResponse(response)
