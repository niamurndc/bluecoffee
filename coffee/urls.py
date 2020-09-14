from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('coffees/', views.coffees, name = 'coffees'),
    path('create/', views.create, name = 'create'),
    path('view/<id>/', views.view, name = 'view'),
    path('delete/<id>/', views.delete_coffee, name = 'delete_coffee'),
    path('login/', views.login_view, name = 'login_view'),
    path('logout/', views.logout_user, name = 'logout_user'),
]