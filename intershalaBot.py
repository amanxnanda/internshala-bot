import requests
import json
from time import sleep
from selenium import webdriver
# # Getting temp email id
def main():
    baseURL = 'https://www.1secmail.com/api/v1/?action='
    authBaseUrl = 'https://internshala.com/registration'
    targetWebsite = 'https://internshala.com/3-day-winternship-camp?utm_source=refer_whatsapp&utm_medium=10508427'
    user_first_name = 'Yaman'
    user_last_name = 'Sharma'


    count = 1
    # Get request for 1 email id
    def gettingEmail(baseURL, count):
        getEmail = requests.get(f'{baseURL}genRandomMailbox&count={count}')
        emailInJson = getEmail.json()
        email = emailInJson[0]
        return email

    email = ''
    while True:
        email = gettingEmail(baseURL, count)
        if(email.find('1secmail') == -1):
            break
    print(email)

    # # Opening browser

    browser = webdriver.Firefox()
    browser.implicitly_wait(5)

    browser.get(targetWebsite)

    email_input = browser.find_element_by_id('email')
    password_input = browser.find_element_by_id('password')
    first_name_input =  browser.find_element_by_id('first_name')
    last_name_input =  browser.find_element_by_id('last_name')



    email_input.send_keys(email)
    password_input.send_keys('WeAreAnonymous777')
    first_name_input.send_keys(user_first_name)
    last_name_input.send_keys(user_last_name)

    sleep(1)

    login_link = browser.find_element_by_xpath('//*[@id="registration-form"]/button')
    login_link.click()

    sleep(10)

    # Spliting the email into login and domain
    emailList = email.split('@')
    login = emailList[0]
    domain = emailList[1]

    # input('Press any key to continue\n')

    # Getting message id
    getMessage = requests.get(f'{baseURL}getMessages&login={login}&domain={domain}')
    messageInJson = getMessage.json()
    messageID = messageInJson[0]["id"]

    # Reading message with 
    readMessage = requests.get(f'{baseURL}readMessage&login={login}&domain={domain}&id={messageID}')

    readMessageInJson = readMessage.json()
    print(readMessageInJson["date"])

    # Extracting url
    bodyHTML = readMessageInJson['body']
    twoPartsBody = bodyHTML.split(authBaseUrl)
    twoPartsBody = twoPartsBody[1]
    twoPartsBody = twoPartsBody.split('"')
    authLink = twoPartsBody[0]
    authLink = authBaseUrl + authLink

    browser.get(authLink)
    sleep(2)
    browser.quit()

if __name__ =='__main__':

    for i in range(6):
        main()
