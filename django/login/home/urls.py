from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('reg/',views.reg),
    path('home/',views.home,name='home'),
    path('logaut/',views.logaut)
]
