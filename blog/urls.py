from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.allblogs, name='allblogs'),
    path('<int:Blog_id>/', views.details, name='details'),
]
