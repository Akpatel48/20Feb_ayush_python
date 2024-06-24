from django.contrib import admin
from django.urls import path,include
from user import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('about/',views.about),
    path('blog/',views.blog),
    path('doctors/',views.doctors),
    path('services/',views.services),
    path('login/',views.login,name='login'),
    path('reg/',views.reg),
    path('userlogout/',views.userlogout),
    path('verify/',views.verifyotp,name='otp')
]