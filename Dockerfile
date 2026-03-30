FROM python:3.11-slim

WORKDIR /app
COPY . /app

RUN pip install torch --index-url https://download.pytorch.org/whl/cpu
RUN pip install -r requirements.txt

CMD ["python3", "app.py"]
