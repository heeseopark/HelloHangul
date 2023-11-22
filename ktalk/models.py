from django.db import models

class ThemeTest(models.Model):
    name = models.CharField(max_length=100)
    inittext = models.TextField()
    assistantrole = models.TextField()

class QuestionTest(models.Model):
    theme = models.ForeignKey(ThemeTest, on_delete=models.CASCADE)
    content = models.TextField()

class AnswerTest(models.Model):
    question = models.OneToOneField(QuestionTest, on_delete=models.CASCADE)
    content = models.TextField()

class ConversationTest(models.Model):
    theme = models.ForeignKey(ThemeTest, on_delete=models.CASCADE)
    role = models.CharField(max_length=10)  # 'user' or 'assistant'
    content = models.TextField()

    def __str__(self):
        return f"{self.role} - {self.theme.name}"