from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Topic
from .forms import TopicForm



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

def new_topic(request):
    ''' display empty form or process user-submitted form'''
    if request.method != 'POST':
        form = TopicForm() # provide empty form if the request is not a form submission
    else: # user submit the form
        form = TopicForm(request.POST)
        if form.is_valid(): # check for validity
            form.save()
            return HttpResponseRedirect(reverse('learning_notes:topics'))
    context = {'form' : form}
    return render(request, 'learning_notes/new_topic.html', context)