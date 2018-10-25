''' URL configuration for learning_notes app'''
from django.urls import path

from . import views

app_name = 'learning_notes'

urlpatterns = [
    path('', views.index, name='index'), # homepage
    path('topics/', views.topics, name = 'topics'), # topics
    path('topics/<int:topic_id>', views.topic, name = 'topic'), # individual topic
]