from django.utils import translation
from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    template_name = "smwebsite/index.html"

    def dispatch(self, request, *args, **kwargs):
        translation.activate(request.LANGUAGE_CODE)
        return super().dispatch(request, *args, **kwargs)


class UcarpoolingHomePageView(TemplateView):
    template_name = "ucarpooling/index.html"

    def dispatch(self, request, *args, **kwargs):
        translation.activate(request.LANGUAGE_CODE)
        return super().dispatch(request, *args, **kwargs)


class SmartmovingHomePageView(TemplateView):
    template_name = "smartmoving/index.html"

    def dispatch(self, request, *args, **kwargs):
        translation.activate(request.LANGUAGE_CODE)
        return super().dispatch(request, *args, **kwargs)


class SmartparkingHomePageView(TemplateView):
    template_name = "smartparking/index.html"

    def dispatch(self, request, *args, **kwargs):
        translation.activate(request.LANGUAGE_CODE)
        return super().dispatch(request, *args, **kwargs)


class BlogHomePageView(TemplateView):
    template_name = "blog/index.html"

    def dispatch(self, request, *args, **kwargs):
        translation.activate(request.LANGUAGE_CODE)
        return super().dispatch(request, *args, **kwargs)


class DisseminationHomePageView(TemplateView):
    template_name = "dissemination/index.html"

    def dispatch(self, request, *args, **kwargs):
        translation.activate(request.LANGUAGE_CODE)
        return super().dispatch(request, *args, **kwargs)


home = HomePageView.as_view()
ucarpooling = UcarpoolingHomePageView.as_view()
smartparking = SmartparkingHomePageView.as_view()
smartmoving = SmartmovingHomePageView.as_view()
blog = BlogHomePageView.as_view()
dissemination = DisseminationHomePageView.as_view()
