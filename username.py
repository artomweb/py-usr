from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import re


instusr = False
twitusr = False
username = raw_input ("Enter a username:")

driver = webdriver.Chrome('./chromedriver')
time.sleep(1)
instaurl = "https://instagram.com/" + username
driver.get(instaurl)

print ("Searching Instagram......")
try:
  elem1 = driver.find_element_by_xpath('/html/body/div/div[1]/div/div/h2')
  if elem1.is_displayed():
    print ("Username not found on Instagram")
    instausr = False
  else:
    print ("elem1 found but not displayed")

except NoSuchElementException:

  try:
      elem2 = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/h1')
      if elem2.is_displayed():
        print ("Username Exists on Instagram")
        instausr = True

      else:
        print ("elem2 found but not displayed")
  except:
    print ("ERROR, continuing..")

if instausr == True:
    element = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[1]/a/span')
    print ("Number of Posts: " + element.text)
    element2 = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span')
    print ("Number of Followers: " + element2.text)
    element3 = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a/span')
    print ("Number of Following: " + element3.text)

twiturl = "https://twitter.com/" + username
driver.get(twiturl)
print ("\n" * 2)
print ("Searching Twitter...")
try:
  elem1 = driver.find_element_by_xpath('/html/body/div[2]/div/h1')
  if elem1.is_displayed():
    print ("Username not found on Twitter")
    twitusr = False
  else:
    print ("elem1 found but not displayed")

except NoSuchElementException:
  
  try:
      elem2 = driver.find_element_by_xpath('//*[@id="page-container"]/div[1]/div/div[1]/div[2]/div[1]/div/a/img')
      if elem2.is_displayed():
        print ("Username Exists on Twitter")
        twitusr = True
      else:
        print ("elem2 found but not displayed")
  except:
    print ("ERROR, continuing..")





if twitusr == True:

    try:
        following = driver.find_element_by_xpath('//*[@id="page-container"]/div[1]/div/div[2]/div/div/div[2]/div/div/ul/li[2]/a/span[3]')
        if following.is_displayed():
            print ("Number of Following: " + following.text)
        else:
            print ("Cannot find Following")

    
    except NoSuchElementException:
         print ("Cannot find Following")
        

    try:
        tweets = driver.find_element_by_xpath('//*[@id="page-container"]/div[1]/div/div[2]/div/div/div[2]/div/div/ul/li[1]/a/span[3]')
        if tweets.is_displayed():
            print ("Number of Tweets: " + tweets.text)
        else:
            print ("Cannot find Tweets")

    except NoSuchElementException:
                
        print ("Cannot find Tweets")

    try:
        followers = driver.find_element_by_xpath('//*[@id="page-container"]/div[1]/div/div[2]/div/div/div[2]/div/div/ul/li[3]/a/span[3]')
        if followers.is_displayed():
            print ("Number of Followers: " + followers.text)
        else:
            print ("Cannot find Followers")

    except NoSuchElementException:
                
        print ("Cannot find Followers")

    try:
        location = driver.find_element_by_xpath('//*[@id="page-container"]/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/span[2]')
        if location.is_displayed():
            print ("Location: " + location.text)
        else:
            print ("Cannot find Location")

    except NoSuchElementException:
                
        print ("Cannot find Location")


    try:
        description = driver.find_element_by_xpath('//*[@id="page-container"]/div[2]/div/div/div[1]/div/div/div/div[1]/p')
        if description.is_displayed():
            print ("Desciption: " + description.text)
        else:
            print ("Cannot find Description")

    except NoSuchElementException:
                
        print ("Cannot find Description")
