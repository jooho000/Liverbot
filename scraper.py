from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import shutil

# Auto-detect Chromium and ChromeDriver paths
CHROME_PATH = shutil.which("chromium") or "/run/current-system/sw/bin/chromium"
CHROMEDRIVER_PATH = shutil.which("chromedriver")

if not CHROME_PATH:
    raise FileNotFoundError("Chromium not found. Run `which chromium` in Replit shell to find its correct path.")

if not CHROMEDRIVER_PATH:
    raise FileNotFoundError("ChromeDriver not found. Run `nix-env -iA nixpkgs.chromedriver` to install it.")

# Ensure ChromeDriver is executable
if not os.access(CHROMEDRIVER_PATH, os.X_OK):
    os.chmod(CHROMEDRIVER_PATH, 0o755)

def scrape_comps(limit=5):
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.binary_location = CHROME_PATH

        service = Service(CHROMEDRIVER_PATH)
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.get("https://www.metatft.com/comps")

        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.ID, "CompListContainer")))

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)

        comp_elements = driver.find_elements(By.CLASS_NAME, "Comp_Title")
        compositions = []

        for comp in comp_elements[:limit]:
            comp_name = comp.text.strip()
            comp_container = comp.find_element(By.XPATH, "./ancestor::div[contains(@class, 'CompRowWrapper')]")

            try:
                unit_elements = comp_container.find_elements(By.CLASS_NAME, "UnitNames")
                units = [unit.text.strip() for unit in unit_elements if unit.text.strip()]
            except:
                units = []

            compositions.append({
                "composition": comp_name,
                "units": units
            })

        driver.quit()
        return compositions if compositions else [{"error": "No compositions found."}]

    except Exception as e:
        return [{"error": str(e)}]

if __name__ == "__main__":
    print(scrape_comps(limit=5))
