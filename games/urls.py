from django.urls import path

from games.views import AnagramHuntView, MathFactsView

app_name = "games"
urlpatterns = [
    path("anagram-hunt/", AnagramHuntView.as_view(), name="anagram-hunt"),
    path("math-facts/", MathFactsView.as_view(), name="math-facts"),
]
