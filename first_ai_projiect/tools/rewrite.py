from first_ai_projiect.app.llm.client import chat
from first_ai_projiect.prompts.templates import REWRITE
def rewrite(text):
    prompt = REWRITE.format(text=text)
    messages = [
        {"role":"user","content":prompt}
    ]
    return chat(messages)