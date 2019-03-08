from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

class Topic(models.Model):
    ''' a topic about which user is learning'''
    text = models.CharField(max_length = 200)
    date_added = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        ''' return a string representation of the model'''
        return self.text

class Entry(models.Model):
    ''' the entry for each topic '''
    owner = models.ForeignKey(User, on_delete = models.CASCADE) # set up user as each entryf's ForeignKey
    topic = models.ForeignKey(Topic, on_delete = models.CASCADE)
    title = models.CharField(max_length = 200)
    # text = models.TextField()
    text = HTMLField()
    date_added = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name_plural = "entries"

    def __str__(self):
        ''' return a string representation of an entry'''
        return self.title
