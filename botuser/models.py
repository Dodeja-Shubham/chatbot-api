from django.db import models

# Create your models here.
class Send_Message(models.Model):
    channel = models.CharField(max_length=100)
    text = models.TextField()
    is_user = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.id)

class Schedule_Message(models.Model):
    channel = models.CharField(max_length=100)
    text = models.TextField()
    post_at = models.DateTimeField()
    is_user = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.id)

class Conversation(models.Model):
    conversation_id = models.CharField(max_length=100)
    conversation_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.conversation_name)
