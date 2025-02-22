import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Auto-detect Chromium and ChromeDriver paths in Docker environment
CHROME_PATH = os.getenv("CHROME_BIN", "/usr/bin/google-chrome-stable")  # Default to google-chrome-stable if not set
CHROMEDRIVER_PATH = os.getenv("CHROMEDRIVER_PATH", "/usr/bin/chromedriver")  # Default to chromedriver if not set

if not CHROME_PATH or not CHROMEDRIVER_PATH:
    raise FileNotFoundError("Chromium or ChromeDriver not found in the expected paths.")

# Setup Selenium with Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")  # Use headless mode since no GUI is available
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")  # Important for reducing resource usage
chrome_options.add_argument("window-size=1280x1024")  # Limit the window size to save resources
chrome_options.add_argument("--remote-debugging-port=9222")  # Optional: Helps with debugging
chrome_options.add_argument("--disable-software-rasterizer")  # Further reduces resource use
chrome_options.add_argument("--disable-extensions")  # Disables unnecessary extensions
chrome_options.add_argument("--disable-logging")  # Disables unnecessary logging
chrome_options.add_argument("--log-level=3")  # Limits log verbosity
chrome_options.binary_location = CHROME_PATH  # Set Chrome binary location dynamically

# Create the service for ChromeDriver
service = Service(CHROMEDRIVER_PATH)

# Initialize the WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

def scrape_comps(limit=3):
    try:
        driver.get("https://www.metatft.com/comps")
        wait = WebDriverWait(driver, 20)  # Increased wait time
        wait.until(EC.presence_of_element_located((By.ID, "CompListContainer")))

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)  # Give time for the page to load more data

        # Update the way to find elements using By.CLASS_NAME
        comp_elements = driver.find_elements(By.CLASS_NAME, "Comp_Title")  # Correct method in Selenium 4
        compositions = []

        for comp in comp_elements[:limit]:  # Only scrape 'limit' number of elements
            comp_name = comp.text.strip()
            comp_container = comp.find_element(By.XPATH, "./ancestor::div[contains(@class, 'CompRowWrapper')]")

            unit_elements = comp_container.find_elements(By.CLASS_NAME, "UnitNames")
            units = [unit.text.strip() for unit in unit_elements if unit.text.strip()]

            compositions.append({
                "composition": comp_name,
                "units": units
            })

        return compositions if compositions else [{"error": "No compositions found."}]
    except Exception as e:
        return [{"error": f"Error during scraping: {str(e)}"}]
    finally:
        # Close the driver session after scraping is done
        driver.quit()

# Run the scraping function
if __name__ == "__main__":
    result = scrape_comps(limit=3)  # Limit to 3
    print(result)
