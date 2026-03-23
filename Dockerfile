FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app
COPY . .

# Expose port
EXPOSE 8080

# Run the app
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8080"]