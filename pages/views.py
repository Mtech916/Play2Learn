import html
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from common.utils.email import send_email
from .forms import ContactUsForm


class ContactUsPageView(FormView):
    template_name = "pages/contact_us.html"
    form_class = ContactUsForm
    success_url = reverse_lazy("pages:thanks")

    def form_valid(self, form):
        data = form.cleaned_data
        to = "agenthiggins@gmail.com"
        subject = "Your message has been received"
        content = f"""<p>Attention Play2Learn Admin!</p>
                <p>Website visitor contact message received:</p>
                <ol>"""
        for key, value in data.items():
            label = key.replace("_", " ").title()
            entry = html.escape(str(value), quote=False)
            content += f"<li>{label}: {entry}</li>"

        content += "</ol>"

        send_email(to, subject, content)
        return super().form_valid(form)


class ContactUsThanksView(TemplateView):
    template_name = "pages/thanks.html"


class HomePageView(TemplateView):
    template_name = "pages/home.html"


class AboutPageView(TemplateView):
    template_name = "pages/about.html"
