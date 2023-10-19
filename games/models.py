from django.conf import settings
from django.db import models
from django.urls import reverse

from common.utils.text import unique_slug


class GameScore(models.Model):
    GAME_CHOICES = [
        ("MATH", "Math Facts Practice"),
        ("ANAGRAM", "Anagram Hunt"),
    ]

    ANAGRAM_SETTINGS = [
        ("3", "3 letter words"),
        ("4", "4 letter words"),
        ("5", "5 letter words"),
        ("6", "6 letter words"),
        ("7", "7 letter words"),
        ("8", "8 letter words"),
    ]

    MATH_OPERATIONS = [
        ("+", "Addition"),
        ("-", "Subtraction"),
        ("x", "Multiplication"),
        ("/", "Division"),
    ]

    # Common Fields
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    game = models.TextField(choices=GAME_CHOICES, default="MATH")
    score = models.IntegerField()

    # Anagram-Hunt specific fields
    word_length = models.CharField(
        max_length=20, choices=ANAGRAM_SETTINGS, null=True, blank=True
    )
    total_words = models.IntegerField(null=True, blank=True)

    # Math-Facts-Practice specific fields
    operation = models.CharField(
        max_length=20, choices=MATH_OPERATIONS, null=True, blank=True
    )
    max_number = models.IntegerField(null=True, blank=True)

    # Read-Only Fields
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
