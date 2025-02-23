# Use the official Selenium image with Chrome pre-installed
FROM selenium/standalone-chrome:latest

# Ensure we are running as the root user
USER root

# Set up a virtual environment for Python
RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"

# Install Python dependencies in the virtual environment
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Set the correct Chrome binary path and ChromeDriver path for Selenium
ENV CHROME_BIN=/usr/bin/google-chrome-stable
ENV CHROMEDRIVER_PATH=/usr/bin/chromedriver

# Copy the project files to the container
COPY . /app
WORKDIR /app

# Expose the appropriate port (Flask default is 5000)
EXPOSE 5000

# Run the bot (ensure your bot's script is named `bot.py`)
CMD ["python3", "bot.py"]
