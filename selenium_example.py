from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
#options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Don't specify chromedriver path!
driver = webdriver.Chrome(options=options)

try:
    driver.get("http://localhost:5005/")
    time.sleep(2)

    print("--= Beginning Tests =--")
    login_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit'][value='Login']")
    copy = driver.find_element(By.CSS_SELECTOR, "p[class='lead']").text

    if copy == "A billion dollars and it's yours!":
        print("[FAILED] - Default Copy is still in place.")
    else:
        print("[PASSED] - Default Copy has been changed.")

    if login_button:
        print("[PASSED] - Login Button Exists.")
    else:
        print("[FAILED] - Login button not found.")

# test actual login
    username = driver.find_element(By.CSS_SELECTOR, "input[type='text'][name='username']")
    username.clear()
    username.send_keys("jeff")

    pw = driver.find_element(By.CSS_SELECTOR, "input[type='password'][name='password']")
    pw.clear()
    pw.send_keys("gumby")
    login_button.click()
    time.sleep(2)

    h1 = driver.find_element(By.CSS_SELECTOR,"h1[id='welcome']")
    print("debug: ", h1.text)
    if "Welcome, jeff" in h1.text:
        print("[PASSED] - Login with username jeff and pw gumby succeeded.")
    else:
        print("[FAILED] - Loging with username jeff and pw gumby failed.")


except Exception as e:
    print("Error:", e)

finally:
    print("--= Ending Tests =--")
    driver.quit()
