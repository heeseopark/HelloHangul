from openai import OpenAI
from .secrets import OPENAI_API_KEY

gpt = OpenAI(api_key=OPENAI_API_KEY)

messages = [{"role": "system", "content": "You are an assistant that provides korean coversation for non-korean users who wants to learn korean. here is the situation: 은행에서 직원한테 계좌개설하는 방법 물어보기. act as if you are having a conversation this the user. so use easy korean vocabulary and try to make as many conversations possible."}]
while True:
    user_content = input("user : ")
    messages.append({"role": "user", "content": f"{user_content}"})

    completion = gpt.chat.completions.create(model="gpt-3.5-turbo", messages=messages)

    assistant_content = completion.choices[0].message.content

    messages.append({"role": "assistant", "content": f"{assistant_content}"})

    print(f"GPT : {assistant_content}")


