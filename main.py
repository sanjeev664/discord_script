from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager import chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import json
import random
import platform
import os
import requests
from nordvpn_connect import initialize_vpn, rotate_VPN, close_vpn_connection

vpn_countries_list = ["Albania", "Costa_Rica", "Greece", "Latvia", "Poland", "Sweden", "Argentina", "Croatia", "Hong_Kong",	"Lithuania", "Portugal", "Switzerland", "Australia", "Cyprus", "Hungary", "Luxembourg", "Romania", "Taiwan", "Austria", "Czech_Republic", "Iceland", "Malaysia", "Serbia", "Thailand", "Belgium", "Denmark", "India", "Mexico", "Singapore", "Turkey", "Bosnia_And_Herzegovina", "Estonia", "Indonesia", "Moldova", "Slovakia", "Ukraine", "Brazil", "Finland", "Ireland", "Netherlands", "Slovenia", "United_Kingdom", "Bulgaria", "France", "Israel", "New_Zealand", "South_Africa", "United_States", "Canada", "Georgia", "Italy", "North_Macedonia", "South_Korea", "Vietnam", "Chile", "Germany", "Japan", "Norway", "Spain"] 


def process_browser_log_entry(entry, data_list):
    data = json.loads(entry['message'])
    try:
        if data['message']['params']['request']['headers']['Authorization'] != "undefined":
            if not data['message']['params']['request']['headers']['Authorization'] in data_list:
                data_list.append(data['message']['params']
                                 ['request']['headers']['Authorization'])
                print("Got token!")
    except:
        pass
    response = json.loads(entry['message'])['message']
    return response


def account_login(username, password):
    chrome_options = Options()
    caps = DesiredCapabilities.CHROME
    caps['loggingPrefs'] = { 'performance':'ALL' }
    chrome_options.add_experimental_option('w3c', False)
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(ChromeDriverManager().install(), desired_capabilities=caps, chrome_options=chrome_options)
    data_list = []
    driver.get("https://discord.com/login")
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div/div/div/form/div/div/div[1]/div[2]/div[1]/div/div[2]/input').send_keys(username)
    driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div/div/div/form/div/div/div[1]/div[2]/div[2]/div/input').send_keys(password)
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div/div/div/form/div/div/div[1]/div[2]/button[2]/div').click()
    time.sleep(60)
    # driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'r')
    # Scrape the token
    driver.get("https://discord.com/channels/@me")
    driver.refresh()
    time.sleep(15)

    # Scrape the log here.
    browser_log = driver.get_log('performance')
    time.sleep(5)
    events = [process_browser_log_entry(entry, data_list) for entry in browser_log]
    print("data_list =>", data_list)
    try:
        driver.quit()
    except:
        pass
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


def email_verification(driver, username, password):
    """
    This function work on the email verification.
    """
    try:
        driver.get("https://webmail.dreamhost.com/")
        time.sleep(5)

        # Enter The Email
        driver.find_element_by_xpath('//*[@id="rcmloginuser"]').send_keys(username)

        # Enter the password
        driver.find_element_by_xpath('//*[@id="rcmloginpwd"]').send_keys(password)

        # Click on the Login button
        driver.find_element_by_id('rcmloginsubmit').click()

        print("Current URL => ", driver.current_url)
        time.sleep(5)
        if driver.current_url != "https://webmail.dreamhost.com/?_task=mail&_mbox=INBOX":
            driver.get("https://webmail.dreamhost.com/?_task=mail&_mbox=INBOX")
        time.sleep(5)

        # click on the gmail message
        driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[4]/table[2]/tbody/tr/td[2]/span[3]/a').click()
        time.sleep(7)
        iframe = driver.find_element_by_tag_name('iframe')

        driver.switch_to.frame(iframe)
        
        # Click on the verify button
        driver.find_element_by_xpath('//*[@id="message-htmlpart1"]/div/div/div[2]/div/table/tbody/tr/td/div/table/tbody/tr[2]/td/table/tbody/tr/td/a').click()
        time.sleep(40)

    except Exception as e:
        print("Error :", e)
        pass

# def nordvpn_close():
    # Whoops! We couldn't connect you to 'India'. Please try again. If the problem persists, contact our customer support.

def nordvpn_start(country_list):
    country = random.choice(vpn_countries_list)
    settings = initialize_vpn(country)
    rotate_VPN(settings)  # actually connect to server
    # YOUR STUFF
    # close_vpn_connection(settings)
    # version = platform.system()
    # country = random.choice(vpn_countries_list)
    # country_list.append(country)

    # if version == 'Linux':
    #     command = "nordvpn connect "+ country +" > /dev/null 2>&1"

    # else:
    #     command = "nordvpn -c -g "+ country +" > /dev/null 2>&1"

    # os.system(command)
    # print(os.system('nordvpn status'))
    time.sleep(10)
    

def get_proxy_ip(new_ip):
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
    driver.get('https://api.ipify.org/')
    ip = driver.find_element_by_tag_name('body').text
    print(f'\nWith Selenium\nIP:\t{ip}')
    new_ip.append(ip)


def account_create(df):
    country_list = []
    new_ip = []
    for i in range(21, len(df)):
        # nordvpn_close()
        nordvpn_start(country_list)
        # get_proxy_ip(new_ip)
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        # print("--proxy-server=http://%s" % new_ip[0])
        # chrome_options.add_argument("--proxy-server=http://%s" % new_ip[0])
        driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
        # try:
        driver.get('https://discord.com/register')
        username = df['emails'][i]
        password = df['password'][i]
        # driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/form/div/div/div[1]/div/input').send_keys("tapendrakaul.pragroot@gmail.com")
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/form/div/div/div[1]/div/input').send_keys(df['emails'][i])
        time.sleep(5)
        # driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/form/div/div/div[2]/div/input').send_keys("tapendrakaul")
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/form/div/div/div[2]/div/input').send_keys(df['emails'][i].split('@')[0])
        time.sleep(5)
        # driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/form/div/div/div[3]/div/input').send_keys(password)
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/form/div/div/div[3]/div/input').send_keys(df['password'][i])
        time.sleep(5)
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/form/div/div/div[4]/div[1]/div[1]/div/div').click()
        time.sleep(5)
        for _ in range(1):
            actions = ActionChains(driver)
            actions.send_keys(Keys.ENTER).perform()
        # driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/form/div/div/div[4]/div[1]/div[2]/div/div/div/div/div[2]/div').click()

        birth_date = random.randint(1, 30)
        birth_year = random.randint(1990, 2000)
        driver.find_element_by_xpath('//*[@id="react-select-3-input"]').send_keys(birth_date)
        driver.find_element_by_xpath('//*[@id="react-select-4-input"]').send_keys(birth_year)
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div/div/form/div/div/div[5]/label/input').click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div/div/form/div/div/div[6]/button').click()
        time.sleep(4)
        time.sleep(60)

        # Call Email verification function with cred
        email_verification(driver, username, password)
        time.sleep(2)
        driver.quit()

        # Call Login Function with driver and username, password
        account_login(username, password)


if __name__ == "__main__":
    df = pd.read_csv('accounts.csv')
    account_create(df)

