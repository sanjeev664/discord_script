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
import names



def get_number(mobile=None):
    url = "http://api.getsmscode.com/vndo.php"
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
    # print(response)
    response = response.content.decode("utf-8")
    # print(response,"dggf")
    return response

# print(get_number(),"number")



def get_sms(phone_number):
    url = "http://api.getsmscode.com/do.php"
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

number=get_number()
print(number,"NUMBER :")
for i in range(0,1):
    First_name = names.get_first_name(gender='male')
    Last__name = names.get_last_name()
    username = names.get_full_name()
    data_frame = pd.DataFrame([username])

    df_read = data_frame.to_csv('output.csv',mode="a" ,header=False)
    driver = webdriver.Chrome(ChromeDriverManager().install())

    driver.get('')
    time.sleep(5)


    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/form/fieldset/div/div[1]/input').send_keys(First_name)   # Entering first name
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/form/fieldset/div/div[2]/input').send_keys(Last__name)    # Entrnig lat name 
   
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/form/div[1]/div[1]/input').send_keys(username.replace(" ","")+str(1708)) #Entering username 
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/form/div[4]/div[3]/input').send_keys(number)       # get number using api.getsmscode.com
    
    time.sleep(60)
    print(get_sms(number),"SMS  :")
    
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[3]/div[1]/div/div/div[1]/div/div[1]/div/div[1]/input').send_keys('dischordbot')       # passwords
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[3]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys('dischordbot')        # confirm passwords
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button').click()
    time.sleep(5)
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div/div[2]/div[1]/label/input').clear()      # get number using api.getsmscode.com
    

    time.sleep(5)
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div/div[1]/div[2]/div/div/div[1]').click()   # click on county div to choose country
    time.sleep(5)
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div/div[1]/div[2]/div/div/div[2]/ul/li[226]').click()   # select Us list 
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button').click()     # click on Next button 







































# ADd mobile number 

# def get_number(mobile=None):
#     url = "http://api.getsmscode.com/usdo.php?"
#     if mobile:
#         payload = {
#             "action": "getmobile",
#             "username": "pay@noborders.net",
            
#             "token": "28e51577147907a17782c72b0eddc0ac",
#             "pid": "66",
#             "mobile": mobile
#         }
# for i in range(0,1):
#     # print(names.get_full_name())
#     First_name = names.get_first_name(gender='male')
#     Last__name = names.get_last_name()
#     username=names.get_full_name()
#     # print(username)
#     data_frame=pd.DataFrame([username])

#     df_read=data_frame.to_csv('output.csv',mode="a" ,header=False)
#     driver=webdriver.Chrome(ChromeDriverManager().install())

#     driver.get('https://login.yahoo.com/account/create?.intl=in&.lang=en-IN&src=ym&activity=header-signin&pspid=1197806870&.done=https%3A%2F%2Fin.mail.yahoo.com%2Fd&specId=yidReg&done=https%3A%2F%2Fin.mail.yahoo.com%2Fd')
#     time.sleep(5)


#     driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/form/fieldset/div/div[1]/input').send_keys(First_name)   # Entering first name
#     driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/form/fieldset/div/div[2]/input').send_keys(Last__name)    # Entrnig lat name 
   
#     driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/form/div[1]/div[1]/input').send_keys(username.replace(" ","")+str(1708)) #Entering username 
#     driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/form/div[4]/div[3]/input').send_keys(get_number())       # get number using api.getsmscode.com
#     driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[3]/div[1]/div/div/div[1]/div/div[1]/div/div[1]/input').send_keys('dischordbot')       # passwords
#     driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[3]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys('dischordbot')        # confirm passwords
#     driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button').click()
#     time.sleep(5)
#     driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div/div[2]/div[1]/label/input').clear()      # get number using api.getsmscode.com
    

#     time.sleep(5)
#     driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div/div[1]/div[2]/div/div/div[1]').click()   # click on county div to choose country
#     time.sleep(5)
#     driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div/div[1]/div[2]/div/div/div[2]/ul/li[226]').click()   # select Us list 
#     driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button').click()     # click on Next button 

#     else:
#         payload = {
#             "action": "getmobile",
#             "username": "pay@noborders.net",
#             "token": "28e51577147907a17782c72b0eddc0ac",
#             "pid": "66"
#         }
#     payload = urlencode(payload)
#     full_url = url + payload
#     response = requests.post(url=full_url)
#     # print(response)
#     response = response.content.decode("utf-8")
#     # print(response,"dggf")
#     return response
# get_number()

# def get_sms(phone_number):
#     url = "http://api.getsmscode.com/usdo.php?"
#     payload = {
#         "action": "getsms",
#         "username": "pay@noborders.net",
#         "token": "28e51577147907a17782c72b0eddc0ac",
#         "pid": "66",
#         "mobile": phone_number,
#         "author": "pay@noborders.net",
#     }
#     payload = urlencode(payload)
#     full_url = url + payload
#     for x in range(6):
#         response = requests.post(url=full_url).text
#         print(response)
#         code = [int(s) for s in response.split() if s.isdigit() if len(s) == 6 if s != 40404]
#         if code:
#             return code[0]
#         if 'code is' in response:
#             otp = response.split("code is ")[1][:6]
#             return otp
#         time.sleep(4)

#     return False


# def ban_number(phone_number="13156904199"):
# for i in range(0,1):
#     # print(names.get_full_name())
#     First_name = names.get_first_name(gender='male')
#     Last__name = names.get_last_name()
#     username=names.get_full_name()
#     # print(username)
#     data_frame=pd.DataFrame([username])

#     df_read=data_frame.to_csv('output.csv',mode="a" ,header=False)
#     driver=webdriver.Chrome(ChromeDriverManager().install())

#     driver.get('https://login.yahoo.com/account/create?.intl=in&.lang=en-IN&src=ym&activity=header-signin&pspid=1197806870&.done=https%3A%2F%2Fin.mail.yahoo.com%2Fd&specId=yidReg&done=https%3A%2F%2Fin.mail.yahoo.com%2Fd')
#     time.sleep(5)


#     driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/form/fieldset/div/div[1]/input').send_keys(First_name)   # Entering first name
#     driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/form/fieldset/div/div[2]/input').send_keys(Last__name)    # Entrnig lat name 
   
#     driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/form/div[1]/div[1]/input').send_keys(username.replace(" ","")+str(1708)) #Entering username 
#     driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/form/div[4]/div[3]/input').send_keys(get_number())       # get number using api.getsmscode.com
#     driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[3]/div[1]/div/div/div[1]/div/div[1]/div/div[1]/input').send_keys('dischordbot')       # passwords
#     driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[3]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys('dischordbot')        # confirm passwords
#     driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button').click()
#     time.sleep(5)
#     driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div/div[2]/div[1]/label/input').clear()      # get number using api.getsmscode.com
    

#     time.sleep(5)
#     driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div/div[1]/div[2]/div/div/div[1]').click()   # click on county div to choose country
#     time.sleep(5)
#     driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div/div[1]/div[2]/div/div/div[2]/ul/li[226]').click()   # select Us list 
#     driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button').click()     # click on Next button 

#         "username": "pay@noborders.net",
#         "token": "28e51577147907a17782c72b0eddc0ac",
#         "pid": "66",
#         "mobile": phone_number,
#         "author": "pay@noborders.net",
#     }
#     payload = urlencode(payload)
#     full_url = url + payload
#     response = requests.post(url=full_url)
#     return response
    
# get_sms()