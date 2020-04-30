# windows build and supported on WSL.
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
from bs4 import BeautifulSoup
import time
import requests
import sys 



#general details
name = input("Enter your name : ")   
print("Hi",name)
reciever_name = input("Enter the reciever's name as mentioned in your whatsapp contacts : ")
moviename = input("Enter the movie name : ").replace(" ","-").title()
print(moviename)



#get script from website
url = "https://www.imsdb.com/scripts/" + moviename +  ".html"
source = requests.get(url).text
if not source: 
    print("No script found.Try another one.")
    sys.exit()
#print(source)




#create soup object for given source request
soup = BeautifulSoup(source,'lxml')
script_movie = soup.find('pre').text                  
if not script_movie :
    print("No script found. Try another one.")
    sys.exit()
#print(script_movie)



#start automating browser
browser = webdriver.Chrome(executable_path = '/mnt/c/ProgramData/chocolatey/bin/chromedriver.exe')  # Add path here
browser.get("https://web.whatsapp.com/")
wait = WebDriverWait(browser,600)        #wait for sipulated time given to open browser


#search for reciever and go to his toolbar
target = '"Nava"'        #name of target  change the target name here
string = script_movie          #message to be sent
x_args = '//span[contains(@title, ' + target + ' )]'       #find the target
target = wait.until(ec.presence_of_element_located((By.XPATH, x_args)))   #wait until target is found
target.click()             #clicks the target


# send the movie script
input_box = browser.find_element_by_class_name('_1Plpp')
input_box.send_keys(script_movie + Keys.ENTER)
