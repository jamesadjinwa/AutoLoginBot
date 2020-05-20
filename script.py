##########################################################
## Purpose : Auto connect to a specific captive portal ###
## On Ubuntu copy this file at /etc/network/if-up.d/   ###
##########################################################


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

import time
import os

###########################################################

#enter the link to the website you want to automate login.
website_link="captive_portal_url"
#enter your login username
username="username"
#enter your login password
password="password"

###########################################################

#enter the element for username input field
element_for_username="username"
#enter the element for password input field
element_for_password="password"
#enter the element for submit button
element_for_submit="Submit"

###########################################################

caps = webdriver.DesiredCapabilities.CHROME.copy()
caps['acceptInsecureCerts'] = True

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")



#browser = webdriver.Safari()	#for macOS users[for others use chrome vis chromedriver]

#uncomment this line,for chrome users.
browser = webdriver.Chrome(desired_capabilities=caps, \
        chrome_options=chrome_options)
# Uncoment these lines if you have a custom location for chromedriver
# browser = webdriver.Chrome('/opt/google/chrome/chromedriver', desired_capabilities=caps, \
# chrome_options=chrome_options)	
browser.get((website_link))	

try:
	username_element = browser.find_element_by_name(element_for_username)
	username_element.send_keys(username)		
	password_element  = browser.find_element_by_name(element_for_password)
	password_element.send_keys(password)
	signInButton = browser.find_element_by_name(element_for_submit)
	signInButton.click()
	
	#### to quit the browser uncomment the following lines ####
	# time.sleep(3)
	browser.quit()
	#time.sleep(1)
	#browserExe = "Chrome"
	#os.system("pkill "+browserExe)
except Exception:
	#### This exception occurs if the element are not found in the webpage.
	print "Some error occured :("

	#### to quit the browser uncomment the following lines ####
	browser.quit()
	browserExe = "Chrome"
	os.system("pkill "+browserExe)
