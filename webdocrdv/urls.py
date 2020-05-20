"""webdocrdv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from design_control.views import (
    home_view, 
    about_view,
    contact_view, 
    service_view, 
    pricing_view, 
    blog_view)
from login.views import Login_View,Logout_View
from Patient.views import Patient_Profile_View
from django.conf import settings
from django.conf.urls.static import static
from registration.views import registration_View

#####-------------Urls Paterns---------#######

urlpatterns = [
    path('index', home_view, name='Home'),
    path('', home_view, name='Home'),
    path('about', about_view, name='About'),
    path('contact', contact_view, name='contact'),
    path('service', service_view, name='service'),
    path('pricing', pricing_view, name='pricing'),
    path('blog', blog_view, name='blog'),
    path('login',Login_View,name='Login'),
    path('registration',registration_View,name='registration'),
    path('logout',Logout_View,name='logout'),
    path('patient_profile',Patient_Profile_View,name='patient_Profile'),



    #±±±±±±±±±±±±±Admin Costum Design Url And Main Url±±±±±±±±±±±±±±±±±±±#
    path('jet/', include('jet.urls', 'jet')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    path('admin/', admin.site.urls),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)