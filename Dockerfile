# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy scripts and data
COPY scripts/ ./scripts/
COPY data/ ./data/

# Entry point
CMD ["python", "./scripts/load_data.py"]
