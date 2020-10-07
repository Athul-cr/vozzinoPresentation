"""Employee URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from Regemp.views import check,Register,index,SignUp,EmpView,EmpEdit,DeletePro
urlpatterns = [
    path("create",check,name="check"),
    path("reg",Register,name="Register"),
    path("index",index,name="index"),
    path("signin",SignUp,name="SignUp"),
    path("empview<int:pk>",EmpView,name="EmpView"),
    path("empedit<int:pk>",EmpEdit,name="EmpEdit"),
    path("del<int:pk>",DeletePro,name="DeletePro"),


]
