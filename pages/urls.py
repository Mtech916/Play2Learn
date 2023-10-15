from django.urls import path

from pages.views import (
    ContactUsPageView,
    ContactUsThanksView,
    HomePageView,
    AboutPageView,
)

app_name = "pages"
urlpatterns = [
    path("", HomePageView.as_view(), name="homepage"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("contact-us/", ContactUsPageView.as_view(), name="contact-us"),
    path("contact-us/thanks/", ContactUsThanksView.as_view(), name="thanks"),
]
