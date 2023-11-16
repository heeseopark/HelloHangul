from django.db import models

# Create your models here.

class ConversationListTest(models.Model):
    question = models.TextField()
    answer = models.TextField()

class ChatListTest(models.Model):
    conversation = models.OneToOneField(ConversationListTest, on_delete=models.CASCADE)

class ThemeListTest(models.Model):
    theme = models.TextField()

class QuizListTest(models.Model):
    question = models.TextField()
    answer = models.TextField()
    theme = models.ForeignKey(ThemeListTest, on_delete=models.CASCADE)
