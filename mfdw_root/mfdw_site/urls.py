from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('quote/', include('quotes.urls')),
    path('', include('pages.urls')),
]
