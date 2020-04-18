from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('',include(('management.urls','management'), namespace='management')),
    path('admin/', admin.site.urls),
]
