from django.shortcuts import render
from django.views.generic import View

# Create your views here.

class Base(View):
    def get(self, request):
        context = {}
        return render(request, 'core/base.html', context)