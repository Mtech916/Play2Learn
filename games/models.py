from django.conf import settings
from django.db import models
from django.urls import reverse

from common.utils.text import unique_slug


class GameScore(models.Model):
    MATH = "MATH"
    ANAGRAM = "ANAGRAM"

    GAME_CHOICES = [(MATH, "Math Facts Practice"), (ANAGRAM, "Anagram Hunt")]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    game = models.TextField(choices=GAME_CHOICES, default=MATH)
    score = models.IntegerField()
    slug = models.SlugField(max_length=50, unique=True, null=False, editable=False)
    created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("games:score-details", args=[str(self.slug)])

    def save(self, *args, **kwargs):
        if not self.slug:
            value = str(self)
            self.slug = unique_slug(value, type(self))

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} played the {self.get_game_display()} game and scored {self.score}."
