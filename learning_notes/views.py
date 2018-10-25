from django.shortcuts import render
from django.http import HttpResponse
from .models import Topic


def index(request):
    ''' homepage'''
    return render(request, 'learning_notes/index.html')

def topics(request):
    ''' main topics page, display all topics'''
    topics = Topic.objects.order_by('date_added')
    context = {'topics' : topics}
    return render(request, 'learning_notes/topics.html', context)

def topic(request, topic_id):
    ''' each individual topic page. Display all entries related to the topic'''
    topic = Topic.objects.get(pk = topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic' : topic, 'entries' : entries}
    return render(request, 'learning_notes/topic.html', context)