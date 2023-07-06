# project/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from lecturers import views as lecturer_views
# from students import views as student_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')), 
    path('api/', include('base.api.urls')),
    path('lecturers/', include('lecturers.urls')),
    path('students/', include('students.urls')),
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)