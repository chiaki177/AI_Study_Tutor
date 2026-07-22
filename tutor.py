from llm import ask_llm
from rag import load_knowledge
from rag import retrieve

def start_chat():
    knowledge = load_knowledge()
    messages = [
    {
        "role":"system",
        "content":""

    }
]
    while True:
        question = input("You: ")

        if question.lower() == "quit":
            print("Conversation Summary")
            print("-"*20)
            for message in messages:
                if message.get("role") == "assistant":
                    role = "AI"
                elif message.get("role") == "user":
                    role = "user"
                else:
                    role = "system"
                if role != "system":
                    content = message.get("content")
                    print(f"{role}:\n{content}")
                else:
                    continue
            break
        else:
            retrieved_knowledge = retrieve(question,knowledge)
            messages[0]["content"] = f"""
You are a helpful AI tutor.

Use the following knowledge:

{retrieved_knowledge}

If the answer is not in the knowledge,
say that you don't know.
"""
            messages.append(
        {
            "role":"user",
            "content":question
         }
)           
            answer = ask_llm(messages)
            print(f"AI:{answer}")
            messages.append(
            {
            "role":"assistant",
            "content":answer
         }
)           

start_chat()        
        
