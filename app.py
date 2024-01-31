from selenium import webdriver
from decouple import config
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd
import numpy as np


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

table = pd.read_excel('TopicsAndEntries.xlsx')
for i,topic in enumerate(table['Topic']):
    topics = table.loc[i, 'Topic']
    entries = table.loc[i, 'Entries']

    driver.get("http://127.0.0.1:8000/users/login")
    username = driver.find_element(By.ID, "id_username")
    password = driver.find_element(By.ID, "id_password")

    username.send_keys(config("USERNAME_TEST"))
    password.send_keys(config("PASSWORD"))
    sleep(3)

    login_attempt = driver.find_element(By.XPATH, '/html/body/form/button').click()

    driver.find_element(By.XPATH, '/html/body/a[1]').click()
    driver.find_element(By.XPATH, '/html/body/a[3]').click()
    sleep(3)
    input_entries = driver.find_element(By.ID, "id_text").send_keys(str(topics))
    driver.find_element(By.XPATH, '/html/body/form/button').click()
    sleep(3)
    topic_xpath = f"//a[contains(text(), '{topics}')]"
    driver.find_element(By.XPATH, topic_xpath).click()
    sleep(3)
    driver.find_element(By.XPATH, '/html/body/p[5]/a').click()
    driver.find_element(By.XPATH, '//*[@id="id_text"]').send_keys(str(entries))
    sleep(3)
    driver.find_element(By.XPATH, '/html/body/form/button').click()
    sleep(3)
    driver.find_element(By.XPATH, '/html/body/a[1]/h1').click()
    


driver.quit()




