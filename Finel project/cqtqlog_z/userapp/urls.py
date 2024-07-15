from django.contrib import admin
from django.urls import path
from userapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('photodetail/',views.photodetail),
    path('about/',views.about),
    path('contact/',views.contac),
    path('login/',views.login, name='login'),
    path('sinup/',views.sinup,name='sinup'),
    path('logout/',views.logogut),

    
]+ static(settings.MEDIA_URL,documet_root=settings.MEDIA_ROOT)