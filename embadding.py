from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import numpy as np

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")

docs=['this is from Mubarak', 'this is from Galbe ','this is from shati']
query = "Select text from Galibe"
vector_docs = embeddings.embed_documents(docs)
vector_query = embeddings.embed_query(query)
#print(vector_docs)
#print(vector_query)

from sklearn.metrics.pairwise import cosine_similarity

similarity = cosine_similarity([vector_query], vector_docs)
print("Cosine Similarity:", similarity) 
best_index = np.argmax(similarity)
best_doc = docs[best_index]
print("Best Document:", best_doc)
 