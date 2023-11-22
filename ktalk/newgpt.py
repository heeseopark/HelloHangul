from openai import OpenAI
from .models import *
from .secrets import OPENAI_API_KEY

class ChatSession:
    def __init__(self, theme_id):
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.theme = ThemeTest.objects.get(id=theme_id)

    def store_message(self, role, content):
        ConversationTest.objects.create(theme=self.theme, role=role, content=content)

    def get_response(self, user_input):
        # Fetch previous conversations for the current theme
        previous_conversations = ConversationTest.objects.filter(theme=self.theme)

        # Build messages list including previous conversations
        messages = [{"role": "system", "content": "You are an assistant helping a non-Korean person learn Korean. Act as if you are having a conversation with the user. So use easy korean vocabulary and try to make as many conversations possible. Start a conversation in this situation: " + self.theme.name + "Here is your role: " + self.theme.assistantrole}]
        messages.extend([{"role": conv.role, "content": conv.content} for conv in previous_conversations])

        # Add current user input
        messages.append({"role": "user", "content": user_input})

        # Generate the assistant's response
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        assistant_message = response.choices[0].message.content

        # Store assistant message
        self.store_message('assistant', assistant_message)

        return assistant_message

