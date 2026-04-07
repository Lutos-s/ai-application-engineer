from first_ai_projiect.app.llm.client import chat
from first_ai_projiect.prompts.templates import KEYWORDS
def keywords(text):
    prompt = KEYWORDS.format(text=text)
    messages =[
        {"role":"user","content":prompt}
    ]
    return chat(messages)