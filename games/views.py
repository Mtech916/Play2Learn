from django.views.generic import TemplateView


class MathFactsView(TemplateView):
    template_name = "games/math-facts.html"


class AnagramHuntView(TemplateView):
    template_name = "games/anagram-hunt.html"
