"""
URL configuration for rest_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from user import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.getall),
    path('getstid/<int:id>',views.getstid),
    path('deleteid/<int:id>',views.deleteid),
    path('insrtdata/',views.insertdata),
    path('update/<int:id>',views.update),
    
    
]
