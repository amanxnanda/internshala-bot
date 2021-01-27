from time import sleep
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
from selenium import webdriver

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

def open_browser(PROXY):
    
    flag = True
    webdriver.DesiredCapabilities.FIREFOX['proxy'] = {
        "httpProxy": PROXY,
        "ftpProxy": PROXY,
        "sslProxy": PROXY,
        "proxyType": "MANUAL",
    }

    browser = webdriver.Firefox()
    try:
        browser.get('https://internshala.com/3-day-winternship-camp?utm_source=eap_copylink&utm_medium=10508427');
        flag = True 
    except:
        flag = False
        browser.quit()
    
    if(flag):
        sleep(2)
        browser.quit()
        return 1
    else:
        return 0
    
  

for PROXY in yield_proxy(ind):
    print(PROXY)
    trueCount += open_browser(PROXY)

print(f'Proxy Count  = {proxyCount}')
print(f'True Count = {trueCount}')