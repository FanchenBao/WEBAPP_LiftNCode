''' Users views'''
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

def register(request):
    ''' register a new user'''
    if request.method != 'POST': # user enter registration page for the first time
        form = UserCreationForm()
    else:
        form = UserCreationForm(data = request.POST)
        if form.is_valid():
            form.save() # save new user
            # log the new user in automatically
            username = request.POST['username']
            password = request.POST['password1']
            authenticated_user = authenticate(username=username, password=password)
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('learning_notes:index')) 
    context = {'form':form}
    return render(request, 'users/register.html', context)

