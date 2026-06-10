from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv  
load_dotenv()

model = ChatMistralAI(model='mistral-small-2506')

messages=[
    SystemMessage(content='You are a helpful assistant'),
    HumanMessage(content='Tell me about LangChain')
]
result = model.invoke(messages)
print(result.content)a =
while True:
    user_input = input("User: ")
    if user_input.lower() == "exit":
        break
    messages.append(HumanMessage(content=user_input))
    result = model.invoke(messages)
    print(f"AI: {result.content}")
    messages.append(AIMessage(content=result.content))  

