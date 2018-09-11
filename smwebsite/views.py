from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    template_name = "smwebsite/index.html"


home = HomePageView.as_view()
