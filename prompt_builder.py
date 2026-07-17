def ask_question():
    prompt = input("Question:")
    return prompt

def build_messages(prompt):
    messages = [
    {
        "role":"system",
        "content":"You are a helpful tutor."
    },
    {
        "role":"user",
        "content":prompt
    }
    ]   
    return messages
