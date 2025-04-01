from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# Create a Service object for Chrome
service = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service)

try:
    driver.get("http://localhost:3000/loginscreen")
    time.sleep(2)

    print("--= Beginning Tests =--")
    login_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit'][value='Login']")
    copy = driver.find_element(By.CSS_SELECTOR,"p[class='lead']").text
    
    if copy == "A billion dollars and it's yours!":
        print("[FAILED] - Default Copy is still in place.")
    else:
        print("[PASSED] - Default Copy has been changed.")

    if login_button:
        print("[PASSED] - Login Button Exists.")
    else:
        print("[FAILED] - Login button not found.")

except Exception as e:
    print("Error:", e)

finally:
    print("--= Ending Tests =--")
    driver.quit()

