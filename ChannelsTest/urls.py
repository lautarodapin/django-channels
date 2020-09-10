# mysite/urls.py
from django.conf.urls import include
from django.urls import path
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('chat/', include('chat.urls')),
    path('admin/', admin.site.urls),
] +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)