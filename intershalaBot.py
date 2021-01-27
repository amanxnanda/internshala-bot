import requests
import json
from time import sleep
from selenium import webdriver
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy


req_proxy = RequestProxy() #you may get different number of proxy when  you run this at each time
proxies = req_proxy.get_proxy_list() #this will create proxy list
ind = []
proxyCount = 0
trueCount = 0
for proxy in proxies:
    if(proxy.country == 'India'):
        proxyCount += 1
        ind.append(proxy)

def yield_proxy(ind):
    for i in ind:
        yield i.get_address()

# # Getting temp email id
def internshala(PROXY):
    baseURL = 'https://www.1secmail.com/api/v1/?action='
    authBaseUrl = 'https://internshala.com/registration'
    targetWebsite = 'https://internshala.com/3-day-winternship-camp?utm_source=refer_whatsapp&utm_medium=10508427'
    user_first_name = 'Yaman'
    user_last_name = 'Sharma'
    user_password = 'WeAreAnonymous777'
    count = 1
    flag = True
    webdriver.DesiredCapabilities.FIREFOX['proxy'] = {
    "httpProxy": PROXY,
    "ftpProxy": PROXY,
    "sslProxy": PROXY,
    "proxyType": "MANUAL",
    }

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
    
    # # Opening browser

    browser = webdriver.Firefox()
    browser.implicitly_wait(3)
    try:
        browser.get(targetWebsite)

        email_input = browser.find_element_by_id('email')
        password_input = browser.find_element_by_id('password')
        first_name_input =  browser.find_element_by_id('first_name')
        last_name_input =  browser.find_element_by_id('last_name')

        email_input.send_keys(email)
        password_input.send_keys(user_password)
        first_name_input.send_keys(user_first_name)
        last_name_input.send_keys(user_last_name)

        sleep(1)

        register_now_button = browser.find_element_by_xpath('//*[@id="registration-form"]/button')
        register_now_button.click()
        flag = True
    except:
        print("Lode lagne wale hai")
        flag = False
        browser.quit()

    if(flag):
    # Spliting the email into login and domain
        emailList = email.split('@')
        login = emailList[0]
        domain = emailList[1]

        # input('Press any key to continue\n')
        sleep(5)

        # Getting message id
        def get_id():
            while True:
                try:
                    getMessage = requests.get(f'{baseURL}getMessages&login={login}&domain={domain}')
                    messageInJson = getMessage.json()
                    messageID = messageInJson[0]["id"]
                except:
                    pass
                else:
                    break
            return messageID
        
        messageID = get_id()

        # Reading message with 
        readMessage = requests.get(f'{baseURL}readMessage&login={login}&domain={domain}&id={messageID}')

        readMessageInJson = readMessage.json()
        

        # Extracting url
        bodyHTML = readMessageInJson['body']
        twoPartsBody = bodyHTML.split(authBaseUrl)
        twoPartsBody = twoPartsBody[1]
        twoPartsBody = twoPartsBody.split('"')
        authLink = twoPartsBody[0]
        authLink = authBaseUrl + authLink

        browser.get(authLink)
        
        browser.quit()
        return 1
    else:
        return 0


for PROXY in yield_proxy(ind):
    trueCount += internshala(PROXY)
print(f'Proxy count = {proxyCount}')
print(f'Account created = {trueCount}')