from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_mistralai import MistralAIEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

from dotenv import load_dotenv
load_dotenv()


doc1 = Document(
    page_content = "This is mubarak from yanam",
    metadata = {"source": "yanam"}
)
    
doc2 = Document(
    page_content = "This is a galibe from paris",
    metadata = {"source": "paris"}
)

doc3 = Document(
    page_content = "This is a Shahataj from India",
    metadata = {"source": "India"}
)
docs = [doc1, doc2, doc3]


embeddings = GoogleGenerativeAIEmbeddings(
      model="gemini-embedding-001"
)


db = Chroma(collection_name="chroma_db12")
db.add_documents(docs)
#db.add_documents(docs)



