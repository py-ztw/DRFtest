from django.contrib import admin
from django.urls import path
from Drfday1 import views

urlpatterns = [
    path('user/', views.user),
    path("users/", views.UserView.as_view()),
    path("users/<str:id>/", views.UserView.as_view()),
    path("userss/", views.UserAPIView.as_view()),
    path("userss/<str:id>/", views.UserAPIView.as_view()),

]
