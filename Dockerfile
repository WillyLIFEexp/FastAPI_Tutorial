# Use the official Python 3.11 slim image as the base
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1   
ENV PYTHONUNBUFFERED=1         

# Install system dependencies required for Scrapy and Airflow
RUN apt-get update && apt-get install -y \
    gcc \
    libxml2-dev \
    libxslt-dev \
    libffi-dev \
    libssl-dev \
    build-essential \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry for package management
RUN pip install poetry

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

RUN poetry config virtualenvs.create false && poetry install 

# Expose port 8000
EXPOSE 8000

# # Install dependencies using Poetry
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]