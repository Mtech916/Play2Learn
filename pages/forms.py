from django import forms

from .models import ContactUs


class ContactUsForm(forms.ModelForm):
    EMAIL_TOPIC = (
        (None, "--Please Choose--"),
        ("general", "General Question"),
        ("technical", "Technical Error"),
        ("request", "Feature Request"),
        ("other", "Not Listed"),
    )

    subject = forms.ChoiceField(choices=EMAIL_TOPIC)

    class Meta:
        model = ContactUs
        fields = (
            "first_name",
            "last_name",
            "subject",
            "email",
            "message",
        )
        widgets = {
            "first_name": forms.TextInput(attrs={"autofocus": True}),
            "message": forms.Textarea(attrs={"cols": "75", "rows": "5"}),
        }
