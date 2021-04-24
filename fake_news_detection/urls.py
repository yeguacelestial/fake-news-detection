from django.urls import path, include
from fake_news_detection import views

urlpatterns = [
    path('', views.index, name="home"),
    path('result/', views.result, name="result")
]
