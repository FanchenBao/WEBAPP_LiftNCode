from django.db import models

class Topic(models.Model):
    ''' a topic about which user is learning'''
    text = models.CharField(max_length = 200)
    date_added = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        ''' return a string representation of the model'''
        return self.text
