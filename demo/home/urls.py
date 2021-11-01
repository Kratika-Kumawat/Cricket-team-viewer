from django.urls import path
from . import views

urlpatterns =[
    path('', views.index,name='index'),
    path('main',views.main,name='main'),
    path('update',views.update,name='update'),
    path('signup', views.signup, name='signup'),
    path('addteam', views.addteam, name='addteam'),
    path('delete', views.delete, name='delete'),
    path('logout', views.logout, name='logout'),
]