from django.conf import settings
from django.db import models
from django.urls import reverse

from common.utils.text import unique_slug


class GameReview(models.Model):
    RATING_CHOICES = [
        (1, "1 star"),
        (2, "2 stars"),
        (3, "3 stars"),
        (4, "4 stars"),
        (5, "5 stars"),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    game = models.CharField(max_length=20)
    rating = models.IntegerField(choices=RATING_CHOICES)
    review = models.TextField()
    is_featured = models.BooleanField(default=False)
    slug = models.SlugField(max_length=50, unique=True, null=False, editable=False)
    created = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("reviews:update", args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            value = str(self)
            self.slug = unique_slug(value, type(self))

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Review by {self.user.username}"
