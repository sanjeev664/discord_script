from selenium import webdriver
import time
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import json
import random
from bs4 import BeautifulSoup


def account_login(driver, username, password):
    """
    This functions work on the 
    """
    data_list = []
    driver.get("https://discord.com/login")
    time.sleep(2)
    driver.find_element_by_xpath(
        '//*[@id="app-mount"]/div[2]/div/div/div/div/form/div/div/div[1]/div[2]/div[1]/div/div[2]/input').send_keys(username)
    driver.find_element_by_xpath(
        '//*[@id="app-mount"]/div[2]/div/div/div/div/form/div/div/div[1]/div[2]/div[2]/div/input').send_keys(password)
    time.sleep(2)
    driver.find_element_by_xpath(
        '//*[@id="app-mount"]/div[2]/div/div/div/div/form/div/div/div[1]/div[2]/button[2]/div').click()
    time.sleep(5)
    # driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'r')
    # Scrape the token
    driver.get("https://discord.com/channels/@me")
    driver.refresh()
    time.sleep(15)


def email_verification(username, password):
    """
    This function work on the email verification.
    """
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
    driver.get("https://webmail.dreamhost.com/")
    time.sleep(5)

    # Enter The Email
    driver.find_element_by_xpath('//*[@id="rcmloginuser"]').send_keys(username)

    # Enter the password
    driver.find_element_by_xpath('//*[@id="rcmloginpwd"]').send_keys(password)

    # Click on the Login button
    driver.find_element_by_id('rcmloginsubmit').click()
    time.sleep(5)
    driver.get("https://webmail.dreamhost.com/?_task=mail&_mbox=INBOX")
    time.sleep(5)

    # click on the gmail message
    driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[4]/table[2]/tbody/tr/td[2]/span[3]/a').click()
    time.sleep(7)
    iframe = driver.find_element_by_tag_name('iframe')

    driver.switch_to.frame(iframe)
    
    # Click on the verify button
    driver.find_element_by_xpath('//*[@id="message-htmlpart1"]/div/div/div[2]/div/table/tbody/tr/td/div/table/tbody/tr[2]/td/table/tbody/tr/td/a').click()

    time.sleep(5)

    # account_login(driver, username, password)

if __name__ == "__main__":
    username = "lionheart@andefi.net"
    password = "zixE!26E"
    email_verification(username, password)