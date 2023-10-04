from django.views.generic import TemplateView


class AnagramHuntView(TemplateView):
    template_name = "games/anagram-hunt.html"


class MathFactsView(TemplateView):
    template_name = "games/math-facts.html"


class MathFactsPlayView(MathFactsView):
    template_name = "games/math-facts-play.html"
