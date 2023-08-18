from django.urls import path, include

urlpatterns = [
    path('', include('views.urls')),
    path('apps/', include('apps.urls')),
]