from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

CHROMEDRIVER_PATH = "/usr/local/bin/chromedriver"
URL = "https://www.metatft.com/comps"

def scrape_comps(limit=5):
    """Extracts the first 'limit' compositions and their associated units from MetaTFT."""
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        service = Service(CHROMEDRIVER_PATH)
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.get(URL)

        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.ID, "CompListContainer")))

        # Scroll down to ensure full content loads
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)

        # Find all compositions
        comp_elements = driver.find_elements(By.CLASS_NAME, "Comp_Title")
        compositions = []

        for comp in comp_elements[:limit]:  # Extract only up to the limit
            comp_name = comp.text.strip()
            comp_container = comp.find_element(By.XPATH, "./ancestor::div[contains(@class, 'CompRowWrapper')]")

            # Find all units (champions) inside this composition
            try:
                unit_elements = comp_container.find_elements(By.CLASS_NAME, "UnitNames")
                units = [unit.text.strip() for unit in unit_elements if unit.text.strip()]
            except:
                units = []

            # Format the output
            compositions.append({
                "composition": comp_name,
                "units": units
            })

        driver.quit()

        return compositions if compositions else [{"error": "No compositions found."}]
    
    except Exception as e:
        return [{"error": str(e)}]

# Run the test script
if __name__ == "__main__":
    comps_data = scrape_comps(limit=5)

    for comp in comps_data:
        if "error" in comp:
            print(f"Error: {comp['error']}")
        else:
            print(f"🛡️ **Composition:** {comp['composition']}")
            print(f"⚔️ **Units:** {', '.join(comp['units'])}\n")
