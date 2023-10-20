from django import forms
from django.contrib.auth import get_user_model

from .models import GameReview


class GameReviewForm(forms.ModelForm):
    class Meta:
        model = GameReview
        fields = (
            "game",
            "rating",
            "review",
        )
        widgets = {
            "review": forms.Textarea(attrs={"cols": "75", "rows": "5"}),
        }
        help_texts = {
            "review": "Tell us how much fun you had. The most exciting reviews will be featured on our website!",
        }
