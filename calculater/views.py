from django.http.response import JsonResponse
from django.views.generic.edit import UpdateView
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect, render, get_object_or_404
import requests
from django.core.exceptions import PermissionDenied
from django.utils.text import slugify
from django.db.models import Q
# Create your views here.


def quant_page(request):
    return render(
        request,
        'calculater/base.html',
    )