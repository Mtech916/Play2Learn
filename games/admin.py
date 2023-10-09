from django.contrib import admin

from games.models import GameScore


@admin.register(GameScore)
class GameScoreAdmin(admin.ModelAdmin):
    model = GameScore
    list_display = ["user_name", "game", "score", "created"]

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return "created"

        return ()
