from flask import Flask, render_template, jsonify, request
from src.helper import download_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain_openai import ChatOpenAI
from langchain_classic.chains import create_retrieval_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from src.prompt import system_prompt
from dotenv import load_dotenv
import os

app = Flask(__name__)





@app.route("/")
def index():
    return render_template('chat.html')

if __name__== '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)