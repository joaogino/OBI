from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Videoaula
# Create your views here.
class IndexView(TemplateView):
    template_name = "public/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lista'] = Videoaula.objects.all()
        return context
    
