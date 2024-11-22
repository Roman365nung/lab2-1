from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
# app_blog /views.py

class HomePageView(TemplateView):
    def get(self,request, **kwargs):
        return render(request, 'Index.html',context=None)
