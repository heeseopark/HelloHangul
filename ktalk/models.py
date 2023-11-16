from django.db import models

class ThemeTest(models.Model):
    name = models.CharField(max_length=100)

class QuestionTest(models.Model):
    theme = models.ForeignKey(ThemeTest, on_delete=models.CASCADE)
    content = models.TextField()

class AnswerTest(models.Model):
    question = models.OneToOneField(QuestionTest, on_delete=models.CASCADE)
    content = models.TextField()
