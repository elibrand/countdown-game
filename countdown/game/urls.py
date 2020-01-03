from django.urls import path
from game import views

app_name = 'game'

urlpatterns = [
    path('', views.index, name='index'),
    path('game/', views.game, name='game'),
    path('high_score/', views.high_score, name='high_score'),
    path('game/name/', views.name, name='name'),
]
