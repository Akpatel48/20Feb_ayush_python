from django.contrib import admin
from django.urls import path,include
from user import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('doctor/',views.doctor,name='doctor'),
    path('aboutus/',views.aboutus),
    path('appointment/',views.appointment,name='appointment'),
    path('sinup/',views.sinup),
    path('login/',views.loginview,name='login'),
    path('logou/',views.logou),
    path('doctor_r/',views.doctor_r, name='rgistesen'),
    path('book_app/',views.book_app,name='book_app'),
    path('deletedata/<int:id>',views.deletedata),
]

'''if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)'''