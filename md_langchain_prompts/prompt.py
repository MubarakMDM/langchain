from langchain_core.prompts import PromptTemplate
from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv  
load_dotenv()
 

tempate = """Hi how are you {myfriend}?"""
prompt = PromptTemplate(
    template=tempate,
    input_variables=[],
)
#print(prompt.invoke({"myfriend": "John"}))
models = ChatMistralAI(temperature=1.5)
#temperature parameter to get same result every tiime. 
#model = models.invoke(prompt.invoke({"myfriend": "John"}))
#print(model.content)

chain = prompt | models

inputs = [
    {"myfriend": "Mubarak"}
    ]

responses = chain.batch(inputs)
for i in responses:
    print(i.content)
