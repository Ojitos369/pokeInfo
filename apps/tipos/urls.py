from django.urls import path

from .api import GetTipos


app_name = "apps_tipos"
urlpatterns = [
    path("get_tipos/", GetTipos.as_view(), name=f"{app_name}_get_tipos"),
]