from common.admin import Play2LearnAdmin

from django.contrib import admin

from reviews.models import GameReview


@admin.register(GameReview)
class GameReviewAdmin(Play2LearnAdmin):
    model = GameReview

    # List Attributes
    date_hierarchy = "updated"
    list_display = [
        "user",
        "game",
        "rating",
        "review",
        "is_featured",
        "created",
        "updated",
    ]
    list_filter = ["user", "game", "rating", "is_featured", "created", "updated"]
    ordering = ["-updated"]

    # Form Attributes
    radio_fields = {"game": admin.HORIZONTAL, "rating": admin.HORIZONTAL}

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ("slug", "created", "updated")

        return ()
