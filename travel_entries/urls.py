

from django.urls import path
from travel_entries.views import EntriesListView, PostCreateView


urlpatterns = [
    path('', EntriesListView.as_view(), name='home'),
    path('addpost/', PostCreateView.as_view(), name='add_post')
]