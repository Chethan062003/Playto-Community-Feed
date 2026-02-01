from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),   # ✅ add this line
    path('api/', include('feed.urls')),
]
