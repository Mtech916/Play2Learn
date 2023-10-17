from django import forms

from .models import GameReview


class GameReviewForm(forms.ModelForm):
    GAME_CHOICES = [
        ("ANAGRAM", "Anagram Hunt"),
        ("MATH", "Math Facts Practice"),
    ]

    game = forms.TextField(choices=GAME_CHOICES)

    class Meta:
        model = GameReview
        fields = (
            "game",
            "review",
        )
        widgets = {
            "review": forms.Textarea(attrs={"cols": "75", "rows": "5"}),
        }
