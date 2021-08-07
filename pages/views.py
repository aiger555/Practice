from django.views import View
from django.shortcuts import render
from .models import Page


def pages_list_view(request):
    pages = Page.objects.all()
    return render(request, 'pages/page_list.html', context={'pages': pages})