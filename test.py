from selenium import webdriver
from selenium.webdriver.chrome.options import  Options
from random import seed

from time import process_time, sleep, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
import pandas as pd
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from openpyxl import load_workbook
import urllib.request
from datetime import datetime
from urllib.request import urlopen
import json
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import requests
# from nordvpn_switcher import initialize_VPN, rotate_VPN, terminate_VPN
from nordvpn_connect import initialize_vpn, rotate_VPN, close_vpn_connection
import random


vpn_countries_list = ["Albania", "Costa_Rica", "Greece", "Latvia", "Poland", "Sweden", "Argentina", "Croatia", "Hong_Kong",	"Lithuania", "Portugal", "Switzerland", "Australia", "Cyprus", "Hungary", "Luxembourg", "Romania", "Taiwan", "Austria", "Czech_Republic", "Iceland", "Malaysia", "Serbia", "Thailand", "Belgium", "Denmark", "India", "Mexico", "Singapore", "Turkey", "Bosnia_And_Herzegovina", "Estonia", "Indonesia", "Moldova", "Slovakia", "Ukraine", "Brazil", "Finland", "Ireland", "Netherlands", "Slovenia", "United_Kingdom", "Bulgaria", "France", "Israel", "New_Zealand", "South_Africa", "United_States", "Canada", "Georgia", "Italy", "North_Macedonia", "South_Korea", "Vietnam", "Chile", "Germany", "Japan", "Norway", "Spain"] 


def process_browser_log_entry(entry, data_list):
    """
    This function work on the get network traffic data:)
    """
    data = json.loads(entry['message'])

    # print("Token => ", data)

    try:
        if data['message']['params']['request']['headers']['Authorization'] != "undefined":
            print("Token =>", data['message']['params']['request']['headers'])
            if not data['message']['params']['request']['headers']['Authorization'] in data_list:
                data_list.append(data['message']['params']['request']['headers']['Authorization'])
            print("Ok")
    except:
        pass

    response = json.loads(entry['message'])['message']

    return response

def nordvpn_start():
    # country = random.choice(vpn_countries_list)
    # settings = initialize_VPN(save=1, area_input=[random.choice(vpn_countries_list)])  # starts nordvpn and stuff
    settings = initialize_vpn(random.choice(vpn_countries_list))
    rotate_VPN(settings)


def discod_login(username, password):
    """
    This function work on the login proccess:)
    """
    nordvpn_start()
    data_list = []
    caps = DesiredCapabilities.CHROME
    caps['goog:loggingPrefs'] = {'performance': 'ALL'}

    # Chrome Option add like maximize, proxy etc.
    chrome_options = Options()
    chrome_options.add_experimental_option('w3c', False)
    driver=webdriver.Chrome(ChromeDriverManager().install(),desired_capabilities=caps, options=chrome_options)
    driver.get('https://discord.com/login') 
    driver.maximize_window()
    time.sleep(5)

    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div/form/div/div/div[1]/div[2]/div[1]/div/div[2]/input').send_keys(username)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div/form/div/div/div[1]/div[2]/div[2]/div/input').send_keys(password)
    time,sleep(3)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div/form/div/div/div[1]/div[2]/button[2]').click()
    time.sleep(40)
    driver.get("https://discord.com/channels/@me")
    driver.refresh()
    time.sleep(15)

    # Scrape the log here.
    browser_log = driver.get_log('performance')
    events = [process_browser_log_entry(entry, data_list) for entry in browser_log]
    print("data_list =>", data_list)
    headers = {
        "Content-Type": "application/json",
    }
    data = {
            "user": 1,
            "username": username,
            "status": "ACTIVE",
            "email": username,
            "phone": "1234567890",
            "password": password,
            "country": "india",
            "auth_token": data_list[0],
            "profile_image": "None",
            "banner_image": "None"
        }
    dd = json.dumps(data)
    print("Json Response => ", dd)
    # res = requests.post("http://127.0.0.1:8000/add_discord_account/", headers=headers, data=dd)
    # print("Responce => ", res)
    events = [event for event in events if 'Network.response' in event['method']]


if __name__ == "__main__":
    # sunilrajputdev@gmail.com|Rajput@1996
    # username="shivamsaini789612@gmail.com"
    # password="875596abc" #| zoepowell@andefi.net,j-yv?-RR
    username = "sunilrajputdev@gmail.com"
    password = "Rajput@1996"
    discod_login(username, password)