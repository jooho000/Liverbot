FROM python:3.9-slim

# Install dependencies for Chromium and ChromeDriver
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    unzip \
    ca-certificates \
    gnupg \
    && curl -sS https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update \
    && apt-get install -y \
    google-chrome-stable \
    chromedriver \
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
ENV CHROME_BIN=/usr/bin/google-chrome-stable
ENV CHROMEDRIVER_PATH=/usr/bin/chromedriver

# Install Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the project files to the container
COPY . /app
WORKDIR /app

# Run the bot with the correct filename
CMD ["python", "bot.py"]
