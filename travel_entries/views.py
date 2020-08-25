from django.shortcuts import render
from .models import TravelEntries
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .forms import AddPost

class EntriesListView(ListView):
    model = TravelEntries
    template_name='base.html'



    def get_queryset(self):
        queryset = TravelEntries.objects.all().order_by('-id')
        return queryset


class PostCreateView(CreateView):
    model = TravelEntries
    template_name = 'addpost.html'
    form_class = AddPost
    success_url = reverse_lazy('home')

