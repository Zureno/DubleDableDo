import mechanize
from http import cookiejar

# def printCookies(url):
#    browser = mechanize.Browser()
#    cookie_jar = cookiejar.LWPCookieJar()
#    browser.set_cookiejar(cookie_jar)
#    page = browser.open(url)
#    for cookie in cookie_jar:
#        print(cookie)
import mechanize


def testProxy(url, proxy):
    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    browser.set_proxies(proxy)
    page = browser.open(url)
    source_code = page.read()
    print(source_code)


url = 'http://ip.nefsc.noaa.gov/'
hmp = {'http': '03.115.14.159:8080'}  ## add the proxy from the hidemyass.com or rmccurdy.com/scripts/proxy/good.txt.
testProxy(url, hmp)


def testUserAgent(url, userAgent):
    browser = mechanize.Browser()
    browser.addheaders = userAgent
    page = browser.open(url)
    source_code = page.read()
    print(source_code)


url1 = 'http://whatismyuseragent.dotdoh.com/'
userAgent = [('User-agent', 'Mozilla/5.0 (X11; U; ''Linux 2.4.2-2 i586; en-US; m18) Gecko/20010131 Netscape6/6.01')]
testUserAgent(url1, userAgent)
