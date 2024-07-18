from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Initialize the Chrome driver
webdriver_path = '/Users/sarthaksingh/Downloads/chromedriver-mac-x64/chromedriver'
service = Service(webdriver_path)
driver = webdriver.Chrome(service=service)

# Open the website
url = "https://forms.gle/WT68aV5UnPajeoSc8"
driver.get(url)

# Filling out all text fields
time.sleep(3) 

text_field_xpath1 = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
text_field1 = driver.find_element(By.XPATH, text_field_xpath1)
text_field1.send_keys('Sarthak Singh')

text_field_xpath2 = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
text_field2 = driver.find_element(By.XPATH, text_field_xpath2)
text_field2.send_keys('9643708502')

text_field_xpath3 = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
text_field3 = driver.find_element(By.XPATH, text_field_xpath3)
text_field3.send_keys('sarthaksingh426@gmail.com')

text_field_xpath4 = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea'
text_field4 = driver.find_element(By.XPATH, text_field_xpath4)
text_field4.send_keys('Gaur Saundaryam, Greater Noida West, UP')

text_field_xpath5 = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input'
text_field5 = driver.find_element(By.XPATH, text_field_xpath5)
text_field5.send_keys('201309')

text_field_xpath6 = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input'
text_field6 = driver.find_element(By.XPATH, text_field_xpath6)
text_field6.send_keys('25062002')

text_field_xpath7 = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input'
text_field7 = driver.find_element(By.XPATH, text_field_xpath7)
text_field7.send_keys('Male')

text_field_xpath8 = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input'
text_field8 = driver.find_element(By.XPATH, text_field_xpath8)
text_field8.send_keys('GNFPYC')

# Submit the form
submit_button_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span'
submit_button = driver.find_element(By.XPATH, submit_button_xpath)
submit_button.click()

# Close the WebDriver
time.sleep(3) 
driver.quit()

print("Form submitted successfully.")