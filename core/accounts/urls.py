from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.login_view, name='login'),
    path('app/logout/', views.logout_view, name='logout'),





    path('register/', views.register, name='register'),
    path('app/dashboard/', views.dashboard, name='dashboard'),
    path('app/list_awards/', views.list_awards, name='list_awards'),
    path('app/my_awards/', views.my_awards, name='my_awards')
]
