from prompt_builder import ask_question
from prompt_builder import build_messages
from llm import ask_llm

def main():
    while True:
        prompt = ask_question()
        if prompt == "quit":
            break
        else:
            messages = build_messages(prompt)
            response = ask_llm(messages)
            print(response)

main()
