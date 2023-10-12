from django.conf import settings
from django.db import models
from django.urls import reverse


class GameScore(models.Model):
    MATH = "MATH"
    ANAGRAM = "ANAGRAM"

    GAME_CHOICES = [(MATH, "Math Facts Practice"), (ANAGRAM, "Anagram Hunt")]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    game = models.TextField(choices=GAME_CHOICES, default=MATH)
    score = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("games:score-details", args=[str(self.pk)])
