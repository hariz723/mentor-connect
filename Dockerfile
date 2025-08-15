# Use lightweight Python base
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Install dependencies first (better caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Run FastAPI with Uvicorn
CMD ["python", "main.py"]
