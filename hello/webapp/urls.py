from django.urls import path
from webapp.views import index_view, stat

urlpatterns = [
    path('', index_view),
    path('statistic/', stat)
]