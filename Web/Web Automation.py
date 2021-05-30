from selenium import webdriver
import time

chrome = webdriver.Chrome('D:\All Git Repository\Hobby-Projects-Python\Web\chromedriver.exe') # Path of the chromedriver
chrome.get('https://docs.google.com/forms/d/e/1FAIpQLSegHw2JICSGQ97PKKn7oM5pL3777EXczKdHwgjIBxU7y8wQCA/viewform?usp=sf_link')  # url
time.sleep(3)

name = "Ira Mondal"
field = chrome.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
field.send_keys(name)

country = "India"
field = chrome.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
field.send_keys(country)

email = "mmondal0907@gmail.com"
field = chrome.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
field.send_keys(email)

field = chrome.find_element_by_xpath('//*[@id="i17"]/div[3]/div')
field.click()

field = chrome.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span')
field.click()

time.sleep(8)
exit()