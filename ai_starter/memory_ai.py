from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()
client = OpenAI(
    api_key= os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
) 
messages =[ {"role":"system","content":"你是一名英语老师"}]

while True:
    user_input = input("问:\n")
    messages.append({"role":"user","content":user_input})
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=messages
    )
    reply=response.choices[0].message.content
    print(f"答：{reply}\n")
    messages.append({"role":"assistant","content":reply})