from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Today


def features(request):
    return render(request, 'features/features.html')


#def about(request):
#    return render(request, "features/about.html")


def faq(request):
    return render(request, "features/faq.html")


def portfolio(request):
    return render(request, "features/portfolio.html")

