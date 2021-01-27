from http_request_randomizer.requests.proxy.requestProxy import RequestProxy


req_proxy = RequestProxy() #you may get different number of proxy when  you run this at each time
proxies = req_proxy.get_proxy_list() #this will create proxy list
ind = []
proxyCount = 0
for proxy in proxies:
    if(proxy.country == 'India'):
        proxyCount += 1
        ind.append(proxy)


def yield_proxy(ind):
    for i in ind:
        yield i.get_address()

# for j in yield_proxy(ind):
#     print(j)

print(proxyCount)

