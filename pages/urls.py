from django.urls import path
from .views import pages_list_view

urlpatterns =[
    path('pages/', pages_list_view, name='page_url')
]