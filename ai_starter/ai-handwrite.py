from openai import OpenAI
import os
from dotenv import load_dotenv
client = OpenAI(
    api_key= os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role":"system","content":"你是一名AI应用工程师助手"},
        {"role":"user","content":"什么是RAG？用简单易懂的话解释"}
    ]
)
print(response.choices[0].message.content)