from config import API_KEY
from openai import OpenAI


def ask_llm(messages):
    client = OpenAI(
    api_key=API_KEY,
    base_url="https://openrouter.ai/api/v1"
)

    response = client.chat.completions.create(
        model = "deepseek/deepseek-chat",
        messages = messages
) 
    return response.choices[0].message.content

