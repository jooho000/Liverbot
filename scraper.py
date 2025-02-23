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

# Setup Selenium with Chromium
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
chrome_options.binary_location = CHROME_PATH  # Set Chrome binary location dynamically

# Initialize Chrome WebDriver with the provided paths
service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service, options=chrome_options)

def scrape_comps(limit=5):
    try:
        # Visit the website
        driver.get("https://www.metatft.com/comps")
        
        # Wait until the main content is loaded
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.ID, "CompListContainer")))

        # Scroll to the bottom of the page
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)  # Give time for the page to load more data

        # Scrape composition data
        comp_elements = driver.find_elements(By.CLASS_NAME, "Comp_Title")
        compositions = []

        # Loop over the compositions and extract data
        for comp in comp_elements[:limit]:
            comp_name = comp.text.strip()
            comp_container = comp.find_element(By.XPATH, "./ancestor::div[contains(@class, 'CompRowWrapper')]")

            try:
                unit_elements = comp_container.find_elements(By.CLASS_NAME, "UnitNames")
                units = [unit.text.strip() for unit in unit_elements if unit.text.strip()]
            except Exception as e:
                units = []
                print(f"Error extracting units for composition '{comp_name}': {e}")

            compositions.append({
                "composition": comp_name,
                "units": units
            })

        # Return compositions or error if none found
        return compositions if compositions else [{"error": "No compositions found."}]

    except Exception as e:
        return [{"error": f"Error during scraping: {str(e)}"}]

    finally:
        # Ensure the driver session is properly closed after scraping
        driver.quit()

# Run the script if this is the main module
if __name__ == "__main__":
    result = scrape_comps(limit=5)
    print(result)
