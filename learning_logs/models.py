from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Topic(models.Model):
    # A topic the user is learning about. 

    # `text = models.CharField(max_length=200)` is creating a field named `text` in the `Topic` model.
    # This field is of type `CharField` and has a maximum length of 200 characters. It is used to
    # store the text of the topic the user is learning about.
    text = models.CharField(max_length=200)
    
    # The line `data_added = models.DateTimeField(auto_now_add=True)` is creating a field named
    # `data_added` in the `Topic` model. This field is of type `DateTimeField` and has the
    # `auto_now_add` attribute set to `True`.
    data_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        # Return a string representation of the model. 
        return self.text
    
class Entry(models.Model):
    # Something specific learned about a topic. 
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    data_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        # Return a string representation of the model.
        return self.text[:50] + "..."