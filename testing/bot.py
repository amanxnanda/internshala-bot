from time import sleep
from selenium import webdriver


targetWebsite = 'https://internshala.com/3-day-winternship-camp?utm_source=refer_whatsapp&utm_medium=10508427'

browser = webdriver.Firefox()
browser.implicitly_wait(5)

browser.get(targetWebsite)


username_input = browser.find_element_by_id('email')
password_input = browser.find_element_by_id('password')

username_input.send_keys('amannanda8@gmail.com')
password_input.send_keys('@Harsh6969')

sleep(2)

login_link = browser.find_element_by_xpath('//*[@id="registration-form"]/button')
login_link.click()

sleep(5)

browser.close()
