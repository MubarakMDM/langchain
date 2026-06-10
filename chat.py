from langchain_mistralai import OpenAIMistralAI
from dotenv import load_dotenv      

load_dotenv()

model  = OpenAIMistralAI(model='mistral-small-2506')

response = model.invoke("What is the capital of France?")   

print(response.content)