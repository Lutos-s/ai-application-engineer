from openai import OpenAI
from dotenv import load_dotenv
import os
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url=("https://api.deepseek.com")
)
def ask_tool(prompt,system="你是一个ai助手"):
        response = client.chat.completions.create(
                model="deepseek.chat",
                messages=[
                        {"role":"system","content":system},
                        {"role":"user","content":prompt}
                ]
        )
        print(response.choices[0].message.content)