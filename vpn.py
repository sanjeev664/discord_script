import platform
import random
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from nordvpn_connect import initialize_vpn, rotate_VPN, close_vpn_connection

vpn_countries_list = ["Albania", "Costa_Rica", "Greece", "Latvia", "Poland", "Sweden", "Argentina", "Croatia", "Hong_Kong",	"Lithuania", "Portugal", "Switzerland", "Australia", "Cyprus", "Hungary", "Luxembourg", "Romania", "Taiwan", "Austria", "Czech_Republic", "Iceland", "Malaysia", "Serbia", "Thailand", "Belgium", "Denmark", "India", "Mexico", "Singapore", "Turkey", "Bosnia_And_Herzegovina", "Estonia", "Indonesia", "Moldova", "Slovakia", "Ukraine", "Brazil", "Finland", "Ireland", "Netherlands", "Slovenia", "United_Kingdom", "Bulgaria", "France", "Israel", "New_Zealand", "South_Africa", "United_States", "Canada", "Georgia", "Italy", "North_Macedonia", "South_Korea", "Vietnam", "Chile", "Germany", "Japan", "Norway", "Spain"] 

# optional, use this on Linux and if you are not logged in when using nordvpn command

settings = initialize_vpn(random.choice(vpn_countries_list))
rotate_VPN(settings)  # actually connect to server

# YOUR STUFF

close_vpn_connection(settings)

# def test():
#     options = Options()
#     options.headless = True
#     driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
#     driver.get('https://api.ipify.org/')
#     ip = driver.find_element_by_tag_name('body').text
#     print(f'\nWith Selenium\nIP:\t{ip}')


# def nordvpn():
#     version = platform.system()
#     country = random.choice(vpn_countries_list)
#     if version == 'Linux':
#         command =  "nordvpn connect "+ country +" > /dev/null 2>&1"

#     else:
#         command =  "nordvpn -c -g "+ country +" > /dev/null 2>&1"

#     print("command => ", command)
#     os.system(command)
#     print("check status => ", os.system("nordvpn status"))
#     time.sleep(10)
#     test()
        
# nordvpn()