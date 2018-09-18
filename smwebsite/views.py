from django.utils import translation
from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    template_name = "smwebsite/index.html"

    def dispatch(self, request, *args, **kwargs):
        translation.activate(request.LANGUAGE_CODE)
        return super().dispatch(request, *args, **kwargs)


home = HomePageView.as_view()
