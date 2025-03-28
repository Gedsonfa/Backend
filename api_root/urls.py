from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include('api_rest.urls'), name='api_rest_urls'),
    path('', lambda request: redirect('api/', permanent=True)),
]