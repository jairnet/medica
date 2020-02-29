from django.shortcuts import render
from django.views.generic import TemplateView
# from . mixins import DashboardLoginRequiredMixin


# Create your views here.
class index(TemplateView):
    template_name = 'users/index.html'