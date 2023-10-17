import html
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    TemplateView,
    UpdateView,
)

from common.utils.email import send_email

from .models import GameReview
from .forms import GameReviewForm


class GameReviewPageView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = GameReview
    form_class = GameReviewForm
    success_message = "Game Review Submitted Successfully"
    success_url = reverse_lazy("reviews:thanks")

    def form_valid(self, form):
        form.instance.user = self.request.user
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


class GameReviewsThanksView(TemplateView):
    template_name = "reviews/thanks.html"


class GameReviewsDeleteView(UserPassesTestMixin, DeleteView):
    model = GameReview
    success_url = reverse_lazy("reviews:reviews")

    def delete(self, request, *args, **kwargs):
        result = super().delete(request, *args, **kwargs)
        return result

    def form_valid(self, form):
        messages.success(self.request, "Game review deleted")
        return super().form_valid(form)

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.user


class GameReviewsDetailView(LoginRequiredMixin, DetailView):
    model = GameReview
    template_name = "reviews/gamereview_detail.html"


class GameReviewsUpdateView(SuccessMessageMixin, UserPassesTestMixin, UpdateView):
    model = GameReview
    form_class = GameReviewForm
    success_message = "Review Updated."

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.user


class ReviewsPageView(TemplateView):
    model = GameReview
    template_name = "reviews/reviews.html"

    def get_context_data(self, **kwargs):
        context = super(ReviewsPageView, self).get_context_data(**kwargs)
        context["anagram_reviews"] = GameReview.objects.filter(
            game__exact="ANAGRAM"
        ).order_by("game")
        context["math_reviews"] = GameReview.objects.filter(
            game__exact="MATH"
        ).order_by("game")
        return context
