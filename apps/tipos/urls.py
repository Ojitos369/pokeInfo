from django.urls import path

from .api import ShowDanio


app_name = "apps_tipos"
urlpatterns = [
    path("show_danio/", ShowDanio.as_view(), name=f"{app_name}_show_danio"),
]