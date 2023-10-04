from django.urls import path

from games.views import AnagramHuntView, MathFactsPlayView, MathFactsView

app_name = "games"
urlpatterns = [
    path("anagram-hunt/", AnagramHuntView.as_view(), name="anagram-hunt"),
    path("math-facts/", MathFactsView.as_view(), name="math-facts"),
    path("math-facts-play/", MathFactsPlayView.as_view(), name="math-facts-play"),
]
