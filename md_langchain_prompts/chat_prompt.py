
from langchain_core.prompts import ChatPromptTemplate
from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
load_dotenv()

model = ChatMistralAI(model='mistral-small-2506')


while True:
    user_input = input("User: ")
    if user_input.lower() == "exit":
        break
    chat_template = ChatPromptTemplate([
        ('system', 'You are a helpful expert'),
        ('human', user_input)
    ])
    prompt = chat_template.invoke({'humen': user_input})
    result = model.invoke(prompt)a =
    print(f"AI: {result.content}")

