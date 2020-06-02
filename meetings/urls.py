from django.urls import path
from . import views

app_name = 'meetings'

urlpatterns = [

    path('<int:id>',views.detail,name="detail"),
    path('rooms',views.room,name="rooms"),
    path('new', views.new, name="new"),
    path('', views.welcome, name="welcome"),


]
