from django.contrib import admin

from games.models import GameScore


@admin.register(GameScore)
class GameScoreAdmin(admin.ModelAdmin):
    model = GameScore
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

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ("slug", "created")

        return ()
