from django.urls import path, include
from fake_news_detection import views

app_name = "fake_news_detection"

urlpatterns = [
    path('', views.index, name="home"),
    path('result/', views.result, name="result"),
    path('satisfaction/', views.satisfaction, name="satisfaction"),
    path('a/', views.a, name="a"),
]
