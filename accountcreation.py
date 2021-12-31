from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import json


def process_browser_log_entry(entry, data_list):
    """
    This function work on the get network traffic data:)
    """
    data = json.loads(entry['message'])
    try:
        if data['message']['params']['request']['headers']['Authorization'] != "undefined":
            if not data['message']['params']['request']['headers']['Authorization'] in data_list:
                data_list.append(data['message']['params']['request']['headers']['Authorization'])
            print("Ok")
    except:
        pass
    response = json.loads(entry['message'])['message']

    return response


def account_login(driver, username, password):
	"""
	This functions work on the 
	"""
	data_list = []
	driver.get("https://discord.com/login")
	time.sleep(2)
	driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div/div/div/form/div/div/div[1]/div[2]/div[1]/div/div[2]/input').send_keys(username)
	driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div/div/div/form/div/div/div[1]/div[2]/div[2]/div/input').send_keys(password)
	time.sleep(2)
	driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div/div/div/form/div/div/div[1]/div[2]/button[2]/div').click()
	time.sleep(5)
	# driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'r')
	# Scrape the token
	driver.get("https://discord.com/channels/@me")
	driver.refresh()
	time.sleep(15)

	# Scrape the log here.
	browser_log = driver.get_log('performance')
	print("browser_log => ", browser_log)
	time.sleep(5)
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


def account_create(df):
	"""
	Account Create with CSV file.
	"""
	chrome_options = Options()
	caps = DesiredCapabilities.CHROME
	chrome_options.add_experimental_option('w3c', False)
	chrome_options.add_argument("--start-maximized")
	for i in range(0, len(df)):
		driver = webdriver.Chrome(ChromeDriverManager().install(), desired_capabilities=caps, chrome_options=chrome_options)
		try:
			driver.get('https://discord.com/register')
			username = df['emails'][i]
			password = df['password'][i]
			driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/form/div/div/div[1]/div/input').send_keys(df['emails'][i])
			time.sleep(5)
			driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/form/div/div/div[2]/div/input').send_keys(df['emails'][i].split('@')[0])
			time.sleep(5)
			driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/form/div/div/div[3]/div/input').send_keys(df['password'][i])
			time.sleep(5)
			driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/form/div/div/div[4]/div[1]/div[1]/div/div').click()
			time.sleep(5)
			for _ in range(1):
					actions = ActionChains(driver)
					actions.send_keys(Keys.ENTER).perform()
			driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/form/div/div/div[4]/div[1]/div[2]/div/div/div/div/div[2]/div').click()
			for _ in range(1):
					actions = ActionChains(driver)
					actions.send_keys(Keys.ENTER).perform()  
			time.sleep(3)        
			for _ in range(7):
					actions = ActionChains(driver)
					actions.send_keys(Keys.DOWN).perform() 
			for _ in range(1):
					actions = ActionChains(driver)
					actions.send_keys(Keys.ENTER).perform()   
			for _ in range(1):
					actions = ActionChains(driver)
					actions.send_keys(Keys.ENTER).perform() 

		except Exception as e:
			print("Error => ", e)
			pass

		time.sleep(5)
		driver.refresh()
		account_login(driver, username, password)


if __name__ == "__main__":
	df = pd.read_csv('accounts.csv') 
	account_create(df)