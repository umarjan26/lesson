
from django.shortcuts import render

# Create your views here.
from webapp.models import Task, STATUS_CHOICES


def index(request):
    task = Task.objects.order_by("-created_at")
    context = {"tasks": task}
    return render(request, "index.html", context)


