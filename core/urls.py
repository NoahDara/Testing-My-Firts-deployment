from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls'), name='dashboard'),
    path('', include('accounts.urls')),
    path('integration/', include('integration.urls')),
    path('school/', include('school.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns += staticfiles_urlpatterns()