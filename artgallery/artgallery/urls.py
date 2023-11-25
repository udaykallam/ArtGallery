from django.contrib import admin
from django.urls import path, include
from. import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.homefunction,name="home"),
    path("about",views.aboutfunction,name="about"),
    path("login/",views.loginPage,name="login"),
    path("signup/",views.signupfunction,name="signup"),
    path("about",views.aboutfunction,name="about"),
    path("userabout",views.userabout,name="userabout"),
    path("decontact",views.decontact,name="decontact"),
    path("home1",views.home1,name="home1"),
    path("",include('adminapp.urls')),
    path("",include('customerapp.urls')),
    path("",include('artistapp.urls')),
    path("checkuserlogin",views.checkuserlogin,name="checkuserlogin"),
    path("userlogout",views.userlogout,name="userlogout"),
    path("adminlogout",views.adminlogout,name="adminlogout"),
    path("product1/",views.pd1,name="Product-1"),

]
