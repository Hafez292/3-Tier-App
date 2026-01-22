FROM python:3.11-slim

WORKDIR /app

# Copy dependency file
COPY requirements.txt .

# Install system dependencies for psycopg2
RUN apt-get update && apt-get install -y \
    build-essential gcc libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

# Run the app with Gunicorn
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:5000"]
