''' URL configuration for learning_notes app'''
from django.urls import path

from . import views

app_name = 'learning_notes'

urlpatterns = [
    path('', views.index, name='index'), # homepage
    path('topics/', views.topics, name = 'topics'), # topics
    path('topics/<int:topic_id>/', views.topic, name = 'topic'), # individual topic
    path('new_topic/', views.new_topic, name = 'new_topic'), # add new topic
    path('topics/<int:topic_id>/new_entry/', views.new_entry, name = 'new_entry'), # add new entry under a topic
    path('topics/<int:topic_id>/<int:entry_id>/edit/', views.edit_entry, name = 'edit_entry'), # edit an entry
    path('topics/<int:topic_id>/<int:entry_id>/delete/', views.delete_entry, name = 'delete_entry'), # delete an entry
    path('archive/<int:user_id>/topics/', views.archive_user_topics, name = 'archive_user_topics'), # display all topics user has posted under
    path('archive/<int:user_id>/<int:topic_id>/', views.archive_user_entries, name = 'archive_user_entries'), # display all entries user has posted under a specific topic
]