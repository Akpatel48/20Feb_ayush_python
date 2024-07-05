from django.contrib import admin
from django.urls import path,include
from user import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('header/',views.header),
    path('doctor/',views.Doctor,name='d'),
    path('aboutus/',views.aboutus),
    path('appointment/',views.appointment),
    path('sinup/',views.sinup),
    path('login/',views.log),
    path('logou/',views.logou),
    path('Rgistesen/',views.form, name='rgistesen'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)