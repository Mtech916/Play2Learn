from django import forms


class ContactUsForm(forms.Form):
    EMAIL_TOPIC = (
        (None, "--Please Choose--"),
        ("general", "General Question"),
        ("technical", "Technical Error"),
        ("request", "Feature Request"),
        ("other", "Not Listed"),
    )
    first_name = forms.CharField()
    last_name = forms.CharField()
    subject = forms.ChoiceField(choices=EMAIL_TOPIC)
    email = forms.EmailField()
    message = forms.CharField()
