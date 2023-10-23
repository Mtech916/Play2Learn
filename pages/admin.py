from common.admin import Play2LearnAdmin

from django.contrib import admin

from .models import ContactUs


@admin.register(ContactUs)
class ContactUsAdmin(Play2LearnAdmin):
    model = ContactUs

    # List Attributes
    date_hierarchy = "created"
    list_display = ["first_name", "last_name", "subject", "created", "updated"]
    list_filter = ["subject", "created", "updated"]
    ordering = ["-created"]

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ("created", "updated")
        return ()
