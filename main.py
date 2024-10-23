#install driver from https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Edge()
driver.get("https://www.google.com") #link to URL to open

#Figure out how to use line below to lock onto web element
#interactionElement = driver.find_elements()