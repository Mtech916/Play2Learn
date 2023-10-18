from django.contrib import admin

from reviews.models import GameReview


@admin.register(GameReview)
class GameReviewAdmin(admin.ModelAdmin):
    model = GameReview
    list_display = ["user", "game", "review", "is_featured", "created", "updated"]

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ("slug", "created", "updated")

        return ()
