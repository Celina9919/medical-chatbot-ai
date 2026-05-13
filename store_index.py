from dotenv import load_dotenv
import os
from pathlib import Path
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone
from pinecone import ServerlessSpec
from src.helper import load_pdf_files, filter_to_minimal_docs, text_splitter, download_embeddings

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not PINECONE_API_KEY or not GOOGLE_API_KEY:
    raise RuntimeError(
        "Missing required environment variables. Set PINECONE_API_KEY and GOOGLE_API_KEY."
    )

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

extracted_data = load_pdf_files(data=str(DATA_DIR))
filter_data = filter_to_minimal_docs(extracted_data)
text_chunks = text_splitter(filter_data)

embeddings = download_embeddings()

pinecone_api_key = PINECONE_API_KEY
pc = Pinecone(api_key=pinecone_api_key)

index_name = "medical-chatbot"

if not pc.has_index(index_name):
    pc.create_index(
        name=index_name,
        dimension=384, # Dimension of the embeddings
        metric="cosine", # Consine similarity
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )

index = pc.Index(index_name)

docsearch = PineconeVectorStore.from_documents(
    documents=text_chunks,
    embedding=embeddings,
    index_name=index_name
)