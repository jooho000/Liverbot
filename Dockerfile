FROM python:3.9-slim

# Install dependencies for headless Chromium and ChromeDriver
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    unzip \
    chromium \
    chromium-driver \
    libgdk-pixbuf2.0-0 \
    libxss1 \
    libappindicator3-1 \
    libindicator7 \
    libnspr4 \
    libnss3 \
    fonts-liberation \
    libasound2 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*  # Remove cached package lists to reduce image size

# Set environment variables for Chrome and ChromeDriver
ENV CHROME_BIN=/usr/bin/chromium
ENV CHROMEDRIVER_PATH=/usr/bin/chromedriver

# Install Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the project files to the container
COPY . /app
WORKDIR /app

# Run the bot with the correct filename
CMD ["python", "bot.py"]
