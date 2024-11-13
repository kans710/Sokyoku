from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

def get_vectorstore(text_chunks):
    # Create an embedding object compatible with FAISS
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    
    # Pass this embedding object to FAISS, which will embed documents as needed
    vectorstore = FAISS.from_texts(text_chunks, embedding=embeddings)
    return vectorstore
