from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.html import format_html

from common.utils.text import unique_slug


class GameReview(models.Model):
    GAME_CHOICES = [
        ("ANAGRAM", "Anagram Hunt"),
        ("MATH", "Math Facts Practice"),
    ]

    RATING_CHOICES = [
        (1, "1 star"),
        (2, "2 stars"),
        (3, "3 stars"),
        (4, "4 stars"),
        (5, "5 stars"),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    game = models.CharField(max_length=20, choices=GAME_CHOICES)
    rating = models.IntegerField(choices=RATING_CHOICES)
    review = models.TextField()
    is_featured = models.BooleanField(default=False)
    slug = models.SlugField(max_length=50, unique=True, null=False, editable=False)
    created = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("reviews:update", args=[self.slug])

    @property
    def game_rating(self):
        full_star = "&#9733;"
        empty_star = "&#9734;"
        stars = ""

        if self.rating == 5:
            stars = full_star * 5
        elif self.rating == 4:
            stars = full_star * 4 + empty_star
        elif self.rating == 3:
            stars = full_star * 3 + empty_star * 2
        elif self.rating == 2:
            stars = full_star * 2 + empty_star * 3
        elif self.rating == 1:
            stars = full_star + empty_star * 4
        else:
            stars = empty_star * 5

        return format_html(stars)

    def save(self, *args, **kwargs):
        if not self.slug:
            value = str(self)
            self.slug = unique_slug(value, type(self))

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Review by {self.user.username}"