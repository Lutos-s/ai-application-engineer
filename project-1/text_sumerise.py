from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)
def sumerize(text):
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role":"system","content":"你是一个专业的文本总结助手，简洁、准确、重点清晰"},
            {"role":"user","content":f"请用3句话总结以下内容:\n{text}"}
        ]
    )
    return response.choices[0].message.content
if __name__ == "__main__":
    print("=== 文本总结工具 ===")
    
    # 输入你想总结的内容
    user_text = input("请输入需要总结的文本：\n")
    
    # 调用总结函数
    result = sumerize(user_text)
    
    # 输出结果
    print("\n===== 总结结果 =====")
    print(result)