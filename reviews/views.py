import html
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Avg
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)

from common.utils.email import send_email

import json
from django.http import JsonResponse

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


class MyReviewsView(ListView):
    model = GameReview
    template_name = "reviews/myreviews_list.html"
    paginate_by = 10
    context_object_name = "my_reviews"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["username"] = self.request.user.username
        return context

    def get_queryset(self):
        user = self.request.user
        qs = GameReview.objects.filter(user=user)
        ordering = ["game"]
        return qs.order_by(*ordering)


class ReviewsPageView(ListView):
    model = GameReview
    paginate_by = 10
    context_object_name = "reviews"

    def get_average_rating(self):
        return GameReview.objects.aggregate(average_rating=Avg("rating"))[
            "average_rating"
        ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["username"] = self.request.user.username
        context["average_rating"] = self.get_average_rating()

        order_fields, order_key, direction = self.get_order_settings()

        context["order"] = order_key
        context["direction"] = direction

        context["order_fields"] = list(order_fields.keys())[:-1]

        return context

    def get_ordering(self):
        order_fields, order_key, direction = self.get_order_settings()

        ordering = order_fields[order_key]

        if direction != "asc":
            ordering = "-" + ordering

        return ordering

    def get_order_settings(self):
        order_fields = self.get_order_fields()
        default_order_key = order_fields["default_key"]
        order_key = self.request.GET.get("order", "-rating")
        direction = self.request.GET.get("direction", "desc")

        if order_key not in order_fields:
            order_key = default_order_key

        return (order_fields, order_key, direction)

    def get_order_fields(self):
        return {
            "rating": "rating",
            "game": "game",
            "default_key": "rating",
        }


def get_game_reviews(request):
    featured_reviews = GameReview.objects.filter(is_featured=True)

    game_reviews = []

    for review in featured_reviews:
        review_data = {
            "username": review.user.username,
            "review": review.review,
        }
        game_reviews.append(review_data)

    game_reviews_json = json.dumps(game_reviews)

    return JsonResponse({"game_reviews": game_reviews_json}, safe=False)
