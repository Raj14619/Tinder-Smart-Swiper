import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service


def navigateToTinderHomepage():
    driver.get('https://tinder.com/')

    time.sleep(3)

    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a").click() #Click login button on homepage

    time.sleep(5)

    driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button").click() # Choose facebook option

    driver.implicitly_wait(5)

    #driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div/div[4]/button[2]").click() #accept cookies

    #WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="u_0_h_WY"]'))).click()

    time.sleep(3)

    driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/form/div/div[1]/div/input").send_keys("Raj14619@gmail.com")
    driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/form/div/div[2]/div/input").send_keys("Rajishere123!")


if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument('C:/Users/Raj/AppData/Local/Google/Chrome/User Data/Default')

    service = Service(r"C:\Program Files\Google\Chrome\Application\chrome.exe")

    driver = webdriver.Chrome(service=service, options=options)

    navigateToTinderHomepage()
