import os
os.environ['PATH'] += r";C:\Program Files\OpenSSL-Win64\bin"
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def test_scores_service(url):
    try:
        options = Options()
        options.add_argument('--headless')  # Run browser in headless mode
        service = Service('/path/to/chromedriver')  
        driver = webdriver.Chrome(service=service, options=options)

        driver.get(url)
        score_element = driver.find_element(By.XPATH, "//h1[contains(text(),'Score')]")
        score_text = score_element.text
        score = int(score_text.split(':')[1].strip())  # Extract and convert the score to int

        driver.quit()
        return 1 <= score <= 1000
    except Exception as e:
        print(f"Error during test: {e}")
        return False

def main_function():
    url = "http://localhost:8777"  
    if test_scores_service(url):
        exit(0)
    else:
        exit(-1)

if __name__ == "__main__":
    main_function()
