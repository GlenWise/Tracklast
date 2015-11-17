from django.views.generic import ListView
from .models import Link, Vote

class LinkListView(ListView):
    model = Link
