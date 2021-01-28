import requests
import json
import time
from selenium import webdriver
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
from selenium.webdriver.firefox.options import Options


# you may get different number of proxy when  you run this at each time
req_proxy = RequestProxy()
proxies = req_proxy.get_proxy_list()  # this will create proxy list
ind = []
proxyCount = 0
trueCount = 0
expected_time = 150
for proxy in proxies:
    if(proxy.country == 'India'):
        proxyCount += 1
        ind.append(proxy)


def yield_proxy(ind):
    for i in ind:
        yield i.get_address()

# # Getting temp email id


def internshala(PROXY, expected_time):
    start_time = time.time()
    baseURL = 'https://www.1secmail.com/api/v1/?action='
    authBaseUrl = 'https://internshala.com/registration'
    targetWebsite = 'https://internshala.com/3-day-winternship-camp?utm_source=refer_whatsapp&utm_medium=10508427'
    user_first_name = 'Yaman'
    user_last_name = 'Sharma'
    user_password = 'WeAreAnonymous777'
    count = 1
    flag = True

    # Get request for 1 email id

    def gettingEmail(baseURL, count):
        getEmail = requests.get(f'{baseURL}genRandomMailbox&count={count}')
        emailInJson = getEmail.json()
        email = emailInJson[0]
        return email

    email = ''
    while True:
        try:
            email = gettingEmail(baseURL, count)
        except:
            return 0
        if(email.find('1secmail') == -1):
            break

    # # Opening browser

    print('adding proxy')
    webdriver.DesiredCapabilities.FIREFOX['proxy'] = {
        "httpProxy": PROXY,
        "ftpProxy": PROXY,
        "sslProxy": PROXY,
        "proxyType": "MANUAL",
    }
    print('this should be visible')
    options = Options()
    options.headless = True

    browser = webdriver.Firefox(options=options)
    browser.implicitly_wait(3)
    try:
        browser.get(targetWebsite)

        email_input = browser.find_element_by_id('email')
        password_input = browser.find_element_by_id('password')
        first_name_input = browser.find_element_by_id('first_name')
        last_name_input = browser.find_element_by_id('last_name')

        email_input.send_keys(email)
        password_input.send_keys(user_password)
        first_name_input.send_keys(user_first_name)
        last_name_input.send_keys(user_last_name)

        time.sleep(1)

        register_now_button = browser.find_element_by_xpath(
            '//*[@id="registration-form"]/button')
        register_now_button.click()
        flag = True
    except:
        print("Exception while interacting with website")
        flag = False
        browser.quit()

        current_time = time.time()

        if(current_time-start_time > expected_time):
            print("Time limit exceeds")
            browser.quit()
        if(flag):
            # Spliting the email into login and domain
            emailList = email.split('@')
            login = emailList[0]
            domain = emailList[1]

            # input('Press any key to continue\n')
            time.sleep(5)

            # Getting message id
            def get_id():
                while True:
                    try:
                        getMessage = requests.get(
                            f'{baseURL}getMessages&login={login}&domain={domain}')
                        messageInJson = getMessage.json()
                        messageID = messageInJson[0]["id"]
                    except:
                        pass
                    else:
                        break
                return messageID

            messageID = get_id()

            # Reading message with
            readMessage = ''
            try:
                readMessage = requests.get(
                    f'{baseURL}readMessage&login={login}&domain={domain}&id={messageID}')
            except:
                print("Exception at Reading Message")
                browser.quit()

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
    try:
        trueCount += internshala(PROXY, expected_time)  
    except:
        continue

print(f'Proxy count = {proxyCount}')
print(f'Account created = {trueCount}')
