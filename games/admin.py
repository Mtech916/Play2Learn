from common.admin import Play2LearnAdmin
from django.contrib import admin

from games.models import GameScore


@admin.register(GameScore)
class GameScoreAdmin(Play2LearnAdmin):
    model = GameScore

    # List Attributes
    date_hierarchy = "created"
    list_display = [
        "user",
        "game",
        "word_length",
        "total_words",
        "operation",
        "max_number",
        "score",
        "created",
    ]
    list_filter = ["game", "created"]
    ordering = ["-created"]

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ("slug", "created")

        return ()
