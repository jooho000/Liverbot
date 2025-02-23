# Use the official Selenium image with Chrome pre-installed
FROM selenium/standalone-chrome:latest

# Ensure we are running as the root user
USER root

# Install required system dependencies for Python packages
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    wget \
    curl \
    unzip \
    libgdk-pixbuf2.0-0 \
    libxss1 \
    libappindicator3-1 \
    libindicator7 \
    libnspr4 \
    libnss3 \
    fonts-liberation \
    python3-venv \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*  # Remove cached package lists to reduce image size

# Set up a virtual environment
RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"

# Install Python dependencies in the virtual environment
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files to the container
COPY . /app
WORKDIR /app

# Expose the appropriate port (Flask default is 5000)
EXPOSE 5000

# Use python3 to run the bot (ensure your bot's script is named `bot.py`)
CMD ["python3", "bot.py"]
