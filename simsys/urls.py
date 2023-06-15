from django.urls import re_path
from simsys import views

urlpatterns = [
    re_path(r'^login/$', views.login),
]
