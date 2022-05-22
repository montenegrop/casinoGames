from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('testApi.urls', namespace='test_api')),
    path('data/', include('rest.urls', namespace='jsons_tests')),
]
