# Use the official Selenium image with Chrome pre-installed
FROM selenium/standalone-chrome:latest

# Set environment variables for Chrome and ChromeDriver
ENV CHROME_BIN=/usr/bin/google-chrome-stable
ENV CHROMEDRIVER_PATH=/usr/bin/chromedriver

# Install Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy your project files to the container
COPY . /app
WORKDIR /app

# Run the bot (ensure your bot's script is named `bot.py`)
CMD ["python", "bot.py"]
