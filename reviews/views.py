import html
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, TemplateView

from common.utils.email import send_email

from .models import GameReview
from .forms import GameReviewForm


class GameReviewPageView(CreateView):
    model = GameReview
    form_class = GameReviewForm
    success_url = reverse_lazy("reviews:thanks")

    def form_valid(self, form):
        data = form.cleaned_data
        to = "agenthiggins@gmail.com"
        subject = "New Game Review"
        content = f"""<h1>New Game Review Alert</h1>
                <p>User game review received:</p>
                <ol style='list-style: none;'>"""
        for key, value in data.items():
            label = key.replace("_", " ").title()
            entry = html.escape(str(value), quote=False)
            content += f"<li>{label}: {entry}</li>"

        content += "</ol>"

        send_email(to, subject, content)
        return super().form_valid(form)
