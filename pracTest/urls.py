"""
URL configuration for web_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('Question1/', views.question1, name="q1"),
    path('edit_order/<str:order_id>/', views.edit_order, name='edit_order'), #1.*
    path('order_list/', views.order_list, name='order_list'),
    path('order_detail/<str:order_id>/', views.order_detail, name='order_detail'),
    path ('make_order', views.make_order, name='make_order'),
]

# *1. Add a way to edit an entry/object and save it in the database. Done!
# *2. Add a way to add an entry into the database. So add another order for a customer.
