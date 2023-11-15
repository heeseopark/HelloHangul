from django.db import models

# Create your models here.


class ChatListTest(models.Model):
    id = models.IntegerField(primary_key=True)
    conversation = models.IntegerField() # one to one mapping with the conversationlisttest table

class ConversationListTest(models.Model):
    id = models.IntegerField(primary_key=True)
    question = models.TextField()
    answer = models.TextField()