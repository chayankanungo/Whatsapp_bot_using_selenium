from selenium import webdriver
from  selenium.common.exceptions import NoSuchElementException
import time, sys

def new_chat(user_name):
    new_chat = driver.find_element_by_xpath('//div[@class="_3qx7_"]')
    new_chat.click()
    new_user= driver.find_element_by_xpath('//div[@class="_3FRCZ copyable-text selectable-text"]')
    new_user.send_keys(user_name)
    try:
        user = driver.find_element_by_xpath('//span[@title= "{}"]'.format(new_user))
        user.click()
    except NoSuchElementException as se:
        print("not found")
    except Exception as e:
        driver.close()
        print(e)
        sys.exit()
#set path of your webdriver
driver = webdriver.Chrome(executable_path= 'C:\\Users\\HP\Downloads\\chromedriver_win32\\chromedriver.exe')
driver.get("https://web.whatsapp.com/")
time.sleep(20)

user_name_list = ["Babla Bhaiya"] #enter your whatsapp contacts
for user_name in user_name_list:
    try:
        user = driver.find_element_by_xpath('//span[@title= "{}"]'.format(user_name))
        user.click()
    except NoSuchElementException as se:
        new_chat(user_name)

    msg_box= driver.find_element_by_xpath('//div[@class = "_3uMse"]')
    msg_box.send_keys("Hello")
    msg_btn = driver.find_element_by_xpath('//button[@class = "_1U1xa"]')
    msg_btn.click()

