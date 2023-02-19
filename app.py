from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from functions import *

options = Options()
options.add_argument("start-maximized")
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
url = 'https://www.bezrealitky.cz/'

if __name__ == '__main__':
    start()
    sleep(20)