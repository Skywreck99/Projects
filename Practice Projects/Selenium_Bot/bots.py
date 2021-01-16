from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\ChromeDriver\chromedriver.exe"
driver = webdriver.Chrome(PATH)

# Use this to log into the MyU System for University of Minnesota Students
def myu_login():
    driver.get("https://myu.umn.edu")
    signin = False
    form = False
    signin = driver.find_element_by_tag_name("h1")
    form = driver.find_element_by_class_name("idp3_form")


    if signin.text == "Sign In" and form:
        username = driver.find_element_by_id("username")
        password = driver.find_element_by_id("password")
        
        with open("info.txt", 'r') as file:
            name = file.readline()
            pin = file.readline()
            username.send_keys(name[:-1])
            password.send_keys(pin)


        submit = driver.find_element_by_name("_eventId_proceed")
        submit.click()

        driver.switch_to.frame("duo_iframe")

        call = driver.find_element_by_id("auth_methods")
        divs = call.find_elements_by_tag_name("div")
        call_me = divs[1].find_element_by_tag_name("button")
        call_me.click()