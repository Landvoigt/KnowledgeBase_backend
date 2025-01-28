from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('category.urls')),
    path('', include('command.urls')),
    path('', include('routine.urls')),
]
