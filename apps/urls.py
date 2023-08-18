from django.urls import path, include

app_name = 'apps'

urlpatterns = [
    path('tipos/', include('apps.tipos.urls')),
]