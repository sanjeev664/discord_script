# from numpy import number
import requests
from time import time
from urllib.parse import urlencode

from selenium import webdriver
from selenium.webdriver.chrome.options import  Options
from random import seed
from random import random
from time import process_time, sleep, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
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
import csv
import os
import re
from openpyxl import load_workbook
import urllib.request
from datetime import datetime
from urllib.request import urlopen
# import names


def get_number(mobile=None):
    url = "http://api.getsmscode.com/usdo.php?"
    if mobile:
        payload = {
            "action": "getmobile",
            "username": "pay@noborders.net",
            "token": "28e51577147907a17782c72b0eddc0ac",
            "pid": "66",
            "mobile": mobile
        }
    else:
        payload = {
            "action": "getmobile",
            "username": "pay@noborders.net",
            "token": "28e51577147907a17782c72b0eddc0ac",
            "pid": "66"
        }
    payload = urlencode(payload)
    full_url = url + payload
    response = requests.post(url=full_url)
    print("API Response =>", response.json())
    response = response.content.decode("utf-8")
    print("Data =>", response)
    return response


def get_sms(phone_number):
    url = "http://api.getsmscode.com/usdo.php?"
    payload = {
        "action": "getsms",
        "username": "pay@noborders.net",
        "token": "28e51577147907a17782c72b0eddc0ac",
        "pid": "66",
        "mobile": phone_number,
        "author": "pay@noborders.net",
    }
    payload = urlencode(payload)
    full_url = url + payload
    for x in range(6):
        response = requests.post(url=full_url).text
        print(response)
        code = [int(s) for s in response.split() if s.isdigit() if len(s) == 6 if s != 40404]
        if code:
            return code[0]
        if 'code is' in response:
            otp = response.split("code is ")[1][:6]
            return otp
        time.sleep(4)

    return False


def ban_number(phone_number):
    url = "http://api.getsmscode.com/usdo.php?"
    payload = {
        "action": "addblack",
        "username": "pay@noborders.net",
        "token": "28e51577147907a17782c72b0eddc0ac",
        "pid": "66",
        "mobile": phone_number,
        "author": "pay@noborders.net",
    }
    payload = urlencode(payload)
    full_url = url + payload
    response = requests.post(url=full_url)
    return response

get_number()