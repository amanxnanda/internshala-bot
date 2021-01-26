from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
from selenium import webdriver

req_proxy = RequestProxy() #you may get different number of proxy when  you run this at each time
proxies = req_proxy.get_proxy_list() #this will create proxy list

# print(proxies[0].get_address())
# print(proxies[0].country)

ind = []
for proxy in proxies:
    if(proxy.country == 'India'):
        ind.append(proxy)
count = 0
for i in ind:
    count = count +1
    print(i.get_address())
print(count)

PROXY = ind[1].get_address()


webdriver.DesiredCapabilities.FIREFOX['proxy'] = {
    "httpProxy": PROXY,
    "ftpProxy": PROXY,
    "sslProxy": PROXY,
    "proxyType": "MANUAL",
}

browser = webdriver.Firefox()
browser.get('https://internshala.com/3-day-winternship-camp?utm_source=refer_whatsapp&utm_medium=10508427')

  