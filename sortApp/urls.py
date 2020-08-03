from django.contrib import admin
from django.urls import path, include

from .views import SortView

urlpatterns = [
    path('', SortView.as_view(), name='sort_url'),
]
