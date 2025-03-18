from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),  # Add this line
]

urlpatterns += i18n_patterns(
    path('', include('main.urls')),  # Your app's URLs
)
