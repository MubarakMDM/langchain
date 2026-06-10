from langchain_core.prompts import load_prompt
from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv

load_dotenv()

prompt = load_prompt("template.json")

template = prompt.invoke({
    "length_input": "short",
    "paper_input": "A research paper on machine learning",
    "style_input": "concise"
})

model = ChatMistralAI()

result = model.invoke(template)

print(result.content)