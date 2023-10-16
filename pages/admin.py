from django.contrib import admin

from .models import ContactUs


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    model = ContactUs
    list_display = ["first_name", "last_name", "subject", "created", "updated"]

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ("created", "updated")
        return ()
