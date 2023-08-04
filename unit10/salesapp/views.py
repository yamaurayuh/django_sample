from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from .models import SalesModel

# Create your views here.
class init(ListView):
    template_name = 'init.html'
    model = SalesModel

class detail(ListView):
    template_name ='detail.html'
    model = SalesModel

    def post(self, request, *args, **kwargs):
        context = {
            'merchandise': request.POST.get('merchandise'),
            'amout': request.POST.get('amout'),
        }
        return render(request, 'detail.html', context)

class result(ListView):
    template_name = 'result.html'
    model = SalesModel
