
# Use the official python image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /workspace/app

# Install system dependencies required for building Python packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    unzip \
    curl \
    build-essential \
    gcc \
    g++ \
    libffi-dev \
    libssl-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file first for better caching
COPY requirements.txt .

# Upgrade pip and setuptools (important for building wheels)
RUN pip install --no-cache-dir --upgrade pip setuptools wheel

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create a new user with UID 10016 for security
RUN addgroup --gid 10013 choreo && \
    adduser --disabled-password --no-create-home --uid 10013 --ingroup choreo choreouser && \
    chown -R 10013:10013 .

# Switch to the unprivileged user
USER 10013

# Ensure the correct user is in effect
RUN whoami && id

# Expose the FastAPI port (8000)
EXPOSE 8000

# Run the application
CMD ["python", "-m", "app.main"]