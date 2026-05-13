# Medical AI Chatbot

A Flask-based medical question-answering chatbot that uses Retrieval-Augmented Generation (RAG). The app embeds local medical PDF content with Hugging Face sentence transformers, stores the vectors in Pinecone, retrieves relevant context, and asks Google Gemini to generate a concise answer.

> This project is for learning and portfolio demonstration only. It is not a medical service and should not be used as a substitute for professional medical advice, diagnosis, or treatment.

## Demo

![Medical AI Chatbot Demo](https://res.cloudinary.com/dekgqo2qn/image/upload/v1774529646/demo_cura_gif_izadaa.gif)

## Key Learning In This Project

- Building a RAG pipeline with document loading, chunking, embeddings, vector search, retrieval and answer generation.
- Connecting Flask to LangChain, Pinecone, and Google Gemini.

## Tech Stack

- Backend: Python, Flask
- LLM: Google Gemini 2.5 Flash
- Embeddings: Hugging Face Sentence Transformers
- Vector database: Pinecone
- RAG framework: LangChain
- Frontend: HTML, CSS, JavaScript
- Deployment: Docker, Docker Hub, GitHub Actions

## Prerequisites

- Python 3.11+
- Docker

## Local Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Celina9919/medical-chatbot-ai.git
cd medical-chatbot-ai
```

### 2. Create and Activate a Virtual Environment

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

The first install/run can take several minutes because the sentence-transformer model and PyTorch dependencies are downloaded.

### 4. Configure Environment Variables

Create a local `.env` file from the example:

Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

macOS/Linux:

```bash
cp .env.example .env
```

Update `.env` with your own keys:

```ini
PINECONE_API_KEY=your_pinecone_api_key
GOOGLE_API_KEY=your_google_api_key
```

Do not commit `.env`. It is intentionally ignored by Git.

### 5. Create the Pinecone Index and Load Documents

Run this once after setting your environment variables:

```bash
python store_index.py
```

This creates a Pinecone index named `medical-chatbot` if it does not already exist, then loads the PDFs in the `data/` folder into that index.

### 6. Run the App

```bash
python app.py
```

Open [http://localhost:8080](http://localhost:8080) in your browser.

## Docker

Build and run the image locally:

```bash
docker build -t medical-chatbot .
docker run --rm -p 8080:8080 --env-file .env medical-chatbot
```

The Docker container expects the Pinecone index to already exist. Run `python store_index.py` locally first, or run the indexing script in an environment that has the same API keys.

## Security Notes

The chatbot returns AI-generated educational information and can be wrong. Users should contact a qualified clinician for personal medical decisions or urgent symptoms.

## Project Structure

```text
.
├── app.py                 # Flask app and RAG chain
├── store_index.py         # Loads PDF content into Pinecone
├── src/
│   ├── helper.py          # PDF loading, text splitting, embeddings
│   └── prompt.py          # Medical assistant system prompt
├── templates/             # Chat UI template
├── static/                # Frontend assets
├── data/                  # Local medical PDF knowledge base
├── Dockerfile
└── requirements.txt
```

## Troubleshooting

- `Missing required environment variables`: confirm `.env` exists and contains both required keys.
- `Pinecone index not found`: run `python store_index.py` before starting the app.
- Slow startup: the Hugging Face embedding model may be downloading on the first run.
- Docker starts but answers fail: confirm the same Pinecone index was populated with the API key used by the container.
