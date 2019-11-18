from django.urls import include, path
from cpb_s00_api.views import hello

urlpatterns = [
    path("", hello),
]
