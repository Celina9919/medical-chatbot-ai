# Medical AI Chatbot

A RAG-based medical chatbot powered by Google Gemini, LangChain, and Pinecone. Ask medical questions and get accurate answers retrieved from a medical knowledge base.

## Tech Stack

- **Backend:** Python, Flask
- **LLM:** Google Gemini 2.5 Flash
- **Embeddings:** HuggingFace Sentence Transformers
- **Vector Database:** Pinecone
- **Framework:** LangChain
- **Frontend:** HTML, CSS, JavaScript
- **Deployment:** Docker, Docker Hub, GitHub Actions CI/CD

## Prerequisites

- Python 3.11+
- Pinecone account and API key
- Google AI API key

## Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/Celina9919/medical-chatbot-ai.git
cd medical-chatbot-ai
```

### 2. Create a virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # Linux/Mac
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the root directory:

```ini
PINECONE_API_KEY=your_pinecone_api_key
GOOGLE_API_KEY=your_google_api_key
```

### 5. Load embeddings into Pinecone

Run this once to index the medical knowledge base:

```bash
python store_index.py
```

### 6. Run the app

```bash
python app.py
```

Open [http://localhost:8080](http://localhost:8080) in your browser.

## Docker

### Build and run locally

```bash
docker build -t medical-chatbot .
docker run -d -e PINECONE_API_KEY=your_key -e GOOGLE_API_KEY=your_key -p 8080:8080 medical-chatbot
```

### Pull from Docker Hub

```bash
docker pull aitam123/medical-chatbot:latest
docker run -d -e PINECONE_API_KEY=your_key -e GOOGLE_API_KEY=your_key -p 8080:8080 aitam123/medical-chatbot:latest
```
