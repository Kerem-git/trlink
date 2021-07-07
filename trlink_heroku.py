from selenium import webdriver
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import random
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options 
import random
import os
agents = [
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Safari/605.1.15",
  "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0",
  "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"
]
def link():
    req_proxy = RequestProxy()
    proxies = req_proxy.get_proxy_list()
    maxNum = len(proxies)
    print("\n \n Max No of Proxies:" + str(maxNum) + "\n \n")

    choice = random.randint(0,9)
    i = 0

    k =random.randint(0, maxNum-1)
    l =random.randint(0, maxNum-1)
    PROXY = proxies[k].get_address()


    webdriver.DesiredCapabilities.CHROME['proxy']={
        "httpProxy":PROXY,
        "ftpProxy":PROXY,
        "sslProxy":PROXY,

        "proxyType":"MANUAL",
    }

    url = "https://aylink.co/sdney"
    

    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("user-agent="+agents[choice])
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

    #driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
    main_window = driver.current_window_handle
    driver.get(url)
    sleep(6)
    driver.find_element_by_css_selector(css_selector="a.btn.btn-go").click()
    sleep(3)
    driver.switch_to.window(window_name=main_window)
    sleep(2)
    driver.find_element_by_css_selector(css_selector="a.btn.btn-go").click()
    sleep(3)
    driver.quit()



for i in range(999999999999999999):
    try:
        link()   
    except:
        pass