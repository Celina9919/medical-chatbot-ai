# Muultilingua Medical Chatbot Assistant

## How to run?

### STEPS:

Clone the repository

```bash
git clone https://github.com/Celina9919/medical-chatbot-ai.git
```

#### STEP 1: Create a conda environment
```bash
conda create -n medibot python=3.10 -y
```

```bash
conda activate medibot
```

### STEP 2: Install the requirements
```bash
pip install -r requirements.txt
```

```ini
PINECONE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
OPENAI_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```


```bash
# run the following command to store embeddings to pinecone
python store_index.py
```

```bash
# Finally run the following command
python app.py
```

```bash
open up localhost:
```

### TECHSTACK USED:

- Python
- LangChain
- Flask
- Gemini
- Pinecone
- UI: HTML, CSS, JavaScript
- Deployment: AWS (Amazon Web Service)