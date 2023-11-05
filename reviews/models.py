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
        full_star = '<i class="fa-solid fa-star text-warning"></i>'
        stars = ""

        if self.rating == 5:
            stars = full_star * 5
        elif self.rating == 4:
            stars = full_star * 4
        elif self.rating == 3:
            stars = full_star * 3
        elif self.rating == 2:
            stars = full_star * 2
        elif self.rating == 1:
            stars = full_star

        return format_html(stars)

    def save(self, *args, **kwargs):
        if not self.slug:
            value = str(self)
            self.slug = unique_slug(value, type(self))

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.rating} star review by {self.user.username}"
