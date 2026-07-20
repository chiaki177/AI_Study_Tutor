from llm import ask_llm

def load_knowledge():
    with open("knowledge.txt","r") as file:
        return file.read()

def start_chat():
    knowledge = load_knowledge()
    messages = [
    {
        "role":"system",
        "content":f"""
        You are a helpful AI tutor.
        use the following knowledge:
        
        {knowledge}
"""
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
        
