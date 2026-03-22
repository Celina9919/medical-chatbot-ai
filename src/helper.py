# Contains utility/helper functions used across the project
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from typing import List
from langchain_core.documents import Document
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from langchain_community.document_loaders import WebBaseLoader
import time
# Extract text from PDF files
def load_pdf_files(data):
    loader = DirectoryLoader(
        data,
        glob="*.pdf",
        loader_cls=PyPDFLoader
    )
    
    documents = loader.load()
    return documents
def get_soup(url):
    response = requests.get(url, headers={"User-Agent": "MedBot/1.0"}, timeout=20)
    response.raise_for_status()
    return BeautifulSoup(response.text, "html.parser")
def get_letter_pages():
    soup = get_soup(START_URL)
    letter_urls = set()

    for a in soup.find_all("a", href=True):
        href = a["href"].strip()
        full_url = urljoin(START_URL, href)

        if "drug_" in full_url and full_url.endswith(".html"):
            letter_urls.add(full_url)

    return sorted(letter_urls)
def get_drug_pages(limit=50):
    letter_pages = get_letter_pages()
    article_urls = set()

    for letter_url in letter_pages:
        try:
            soup = get_soup(letter_url)

            for a in soup.find_all("a", href=True):
                href = a["href"].strip()
                full_url = urljoin(letter_url, href)

                if (
                    "medlineplus.gov/druginfo/meds/" in full_url
                    and full_url.endswith(".html")
                    and "/drug_" not in full_url
                ):
                    article_urls.add(full_url)

            time.sleep(1)

        except Exception as e:
            print(f"Failed: {letter_url}", e)

    return list(article_urls)[:limit]
def load_medlineplus_docs(limit=50):
    urls = get_drug_pages(limit)
    docs = []

    for url in urls:
        try:
            loader = WebBaseLoader(url)
            docs.extend(loader.load())
            print(f"Loaded: {url}")
            time.sleep(1)
        except Exception as e:
            print(f"Failed loading {url}: {e}")

    return docs

def filter_to_minimal_docs(docs: List[Document]) -> List[Document]:
    """
        Given a list of Document objects, return a new list of Document objects
        containing only 'source' in metadata and the original page_content.
    """
    
    minimal_docs: List[Document] = []
    for doc in docs:
        src = doc.metadata.get("source")
        minimal_docs.append(
            Document(
                page_content=doc.page_content,
                metadata={"source": src}
            )
        )
    
    return minimal_docs

# Split the documents into smaller chunks
def text_splitter(minimal_docs):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500, # each chunk has 500 tokens
        chunk_overlap=20,
        length_function=len
    )
    texts_chunk = text_splitter.split_documents(minimal_docs)
    return texts_chunk

def download_embeddings():
    """
    Download and return the HuggingFace embeddings model.
    """
    model_name = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
    embeddings = HuggingFaceEmbeddings(
        model_name=model_name
    )
    
    return embeddings
embedding = download_embeddings()