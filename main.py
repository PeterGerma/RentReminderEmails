# This Python script will send reminder e-mails to tenants who have oustanding balances on apartments.com to avoid a late fee

import datetime as dt
from email.message import EmailMessage
import smtplib
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import Chrome


fromEmail = 'peter.germa@gmail.com'

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def populateEmail():
    msg = EmailMessage()

    url = 'https://www.amazon.ca/Logitech-Master-Advanced-Wireless-Mouse/dp/B07S395RWD/ref=sr_1_4?dchild=1&keywords=mouse%2Bmx3&qid=1634182753&sr=8-4&th=1'

    msg['Subject'] = 'Reminder to Pay Outstanding Rent Balance'
    msg['From'] = fromEmail
    msg['To'] = fromEmail
    msg.set_content(url)

    return msg

def sendEmail(emailMsg):
    smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465) #Connecting to GMAIL SMTP Server

    # Gmail requires this special app password -> getting from windows env variable
    appPassword = os.environ.get('GMAIL_APP_PASSWORD')

    print('App Password: ' + appPassword)

    #smtp.login(fromEmail, appPassword)
    #smtp.send_message(emailMsg)
    #smtp.close()

def printElement(element):
    element_text = element.text
    element_attribute_value = element.get_attribute('value')
    print('------------------------------------------------------------------------------------------')
    print(element)
    print('element.text: {0}'.format(element_text))
    print('element.get_attribute(\'value\'): {0}'.format(element_attribute_value))

def updateTenantData():

    driver = webdriver.Chrome('C:/Program Files/Google/Chrome Beta/Application/chrome.exe')


    driver.get("https://www.apartments.com/")

    #Waiting to make sure driver is not too fast
    driver.implicitly_wait(15)

    #element = driver.find_element(By.ID, "headerLoginSection")

    #Finds the Sign In button by title
    element = driver.find_element(By.XPATH, "//a[@title='Sign In']")
    printElement(element)

    element.click()

    loginElement = driver.find_element(By.ID, 'iFrameResizer0')
    printElement(loginElement)

    allSubElements = loginElement.find_elements(By.XPATH, "./child::*")
    for element in allSubElements:
        print(element)

    time.sleep(15)

    driver.quit()




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    updateTenantData()
    emailMsg = populateEmail()
    sendEmail(emailMsg)

