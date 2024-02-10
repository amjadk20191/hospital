
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),

    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('doctor/', include('doctor.urls')),
    path('patient/', include('patient.urls')),
    path('phddamin/', include('hospitaladmin.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
