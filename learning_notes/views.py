''' learning_notes views'''
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Topic, Entry
from .forms import TopicForm, EntryForm



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

@login_required
def new_topic(request):
    ''' Add a new topic
        display empty form or process user-submitted form
    '''
    topicAlreadyExist = False # flag
    if request.method != 'POST':
        form = TopicForm() # provide empty form if the request is not a form submission
    else: # user submit the form
        form = TopicForm(data = request.POST)
        if form.is_valid(): # check for validity
            new_topic = form.save(commit = False)
            if Topic.objects.filter(text = new_topic.text).exists(): # check whether the new topic already exists
                topicAlreadyExist = True # use this flag to print warning msg in html template when duplicate topic is entered
            else:
                new_topic.save()
                return HttpResponseRedirect(reverse('learning_notes:topics'))
    context = {'form':form, 'topicAlreadyExist':topicAlreadyExist, 'existingTopic':new_topic}
    return render(request, 'learning_notes/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    ''' Add a new entry under a certain topic
        display empty form or process user-submitted form
    '''
    topic = Topic.objects.get(id = topic_id)
    if request.method != 'POST':
        form = EntryForm() # provide empty form if the request is not a form submission
    else: # user submit the form
        form = EntryForm(data = request.POST)
        if form.is_valid(): # check for validity
            new_entry = form.save(commit = False)
            new_entry.topic = topic
            new_entry.owner = request.user
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_notes:topic', args = [topic_id]))
    context = {'form' : form, 'topic':topic}
    return render(request, 'learning_notes/new_entry.html', context)

@login_required
def edit_entry(request, topic_id, entry_id):
    '''edit an entry'''
    topic = Topic.objects.get(id = topic_id)
    entry = Entry.objects.get(id = entry_id)
    if entry.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = EntryForm(instance = entry) # fill the form with pre-existing data
    else:
        form = EntryForm(instance = entry, data = request.POST) # fill with pre-existing data first, but then update the data based on request.POST
        if form.is_valid(): # check for validity
            form.save()
            return HttpResponseRedirect(reverse('learning_notes:topic', args = [topic_id]))
    context = {'form':form, 'topic':topic, 'entry':entry}
    return render(request, 'learning_notes/edit_entry.html', context)

# @login_required
# def delete_topic(request, topic_id):
#     ''' delete a topic, its entries will be deleted as well'''
#     if topic.owner != request.user:
#         raise Http404
#     topic = Topic.objects.get(id = topic_id)
#     topic.delete()
#     return HttpResponseRedirect(reverse('learning_notes:topics'))

@login_required
def delete_entry(request, topic_id, entry_id):
    ''' delete a topic, its entries will be deleted as well'''
    entry = Entry.objects.get(id = entry_id)
    if entry.owner != request.user:
        raise Http404
    entry.delete()
    return HttpResponseRedirect(reverse('learning_notes:topic', args = [topic_id]))




