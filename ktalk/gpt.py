from .models import *
from openai import OpenAI
from .secrets import OPENAI_API_KEY

class ChatSession:
    def __init__(self, theme_id):
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.theme = ThemeTest.objects.get(id=theme_id)
        inittext = "You are an assistant helping a non-korean person learning korean. Start a conversion in this situation: "
        self.messages = [{"role": "system", "content": inittext + self.theme.name}]

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
            answer = AnswerTest.objects.get(question=last_question)
            answer.content = content
            answer.save()

    def get_response(self, user_message):
        self.append_message(user_message, "user")
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=self.messages
        )
        assistant_message = response.choices[0].message.content
        self.append_message(assistant_message, "assistant")
        return assistant_message


# 매번 저장하고 다시 부르는 방식으로 바꿔야 함.