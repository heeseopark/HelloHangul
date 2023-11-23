from openai import OpenAI
from .secrets import OPENAI_API_KEY

class ChatSession:
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.messages = [{"role": "system", "content": "You are an assistant that provides korean coversation for non-korean users who wants to learn korean. here is the situation: 은행에서 직원한테 계좌개설하는 방법 물어보기. act as if you are having a conversation this the user"}]

    def append_message(self, content, role):
        self.messages.append({"role": role, "content": content})
        #print("executed append_message")

    def get_response(self, user_message):
        self.append_message(user_message, "user")
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=self.messages
        )
        assistant_message = response.choices[0].message.content
        self.append_message(assistant_message, "assistant")
        #print("executed get_response")
        return assistant_message

session = ChatSession()

while True:
    # Prompt the user for input
    user_input = input("Enter your message (or type 'exit' to end): ")

    # Check if the user wants to exit
    if user_input.lower() == 'exit':
        print("Exiting the conversation.")
        break

    # Get the response from the chat session
    assistant_response = session.get_response(user_input)

    # Print the assistant's response
    print("Assistant:", assistant_response)