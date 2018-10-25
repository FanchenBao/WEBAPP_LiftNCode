from django.db import models

class Topic(models.Model):
    ''' a topic about which user is learning'''
    text = models.CharField(max_length = 200)
    date_added = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        ''' return a string representation of the model'''
        return self.text

class Entry(models.Model):
    ''' the entry for each topic '''
    topic = models.ForeignKey(Topic, on_delete = models.CASCADE)
    title = models.CharField(max_length = 200, default = "Add A Title")
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name_plural = "entries"

    def __str__(self):
        ''' return a string representation of an entry'''
        return self.title
