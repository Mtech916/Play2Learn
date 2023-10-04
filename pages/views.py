from django.views.generic import TemplateView


class ContactUsPageView(TemplateView):
    template_name = "pages/contact.html"


class HomePageView(TemplateView):
    template_name = "pages/home.html"


class AboutPageView(TemplateView):
    template_name = "pages/about.html"
