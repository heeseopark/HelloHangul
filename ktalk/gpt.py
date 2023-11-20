# from openai import OpenAI
# from .models import *
# client = OpenAI()

# response = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant."},
#         {"role": "user", "content": "Who won the world series in 2020?"},
#         {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
#         {"role": "user", "content": "Where was it played?"}
#     ]
# )

# system_text = ThemeTest.inittext

from models import *
from openai import OpenAI

class ChatSession:
    def __init__(self, theme_id):
        self.client = OpenAI()
        self.theme = ThemeTest.objects.get(id=theme_id)
        self.messages = [{"role": "system", "content": self.theme.inittext}]

    def append_message(self, content, role):
        self.messages.append({"role": role, "content": content})
        self.store_message(content, role)

    def store_message(self, content, role):
        if role == "user":
            question = QuestionTest.objects.create(theme=self.theme, content=content)
            AnswerTest.objects.create(question=question)  # Placeholder for future answer
        elif role == "assistant":
            # Assuming the last question asked is the one being answered
            last_question = QuestionTest.objects.filter(theme=self.theme).last()
            last_question.answertest.content = content
            last_question.answertest.save()

    def get_response(self, user_message):
        self.append_message(user_message, "user")
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=self.messages
        )
        assistant_message = response['choices'][0]['message']['content']
        self.append_message(assistant_message, "assistant")
        return assistant_message

# Usage Example
session = ChatSession(theme_id=1)
assistant_response = session.get_response("Who won the world series in 2020?")
print(assistant_response)  # Use this response in your application
