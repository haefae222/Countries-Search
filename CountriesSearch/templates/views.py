from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.views.generic import ListView
from django.db.models import Q

def Index(request):
    countries = MyCountries.objects.all()
    return render(request, 'Index.html', {'countries': countries})

class Results(ListView):
    model = MyCountries
    template_name = 'results.html'


    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = MyCountries.objects.filter(
            Q(name__icontains=query)

        )
        return object_list