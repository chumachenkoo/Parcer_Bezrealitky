from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from bs4 import BeautifulSoup
from app import browser, url


def start():
    browser.get(url)
    sleep(2)

    input_tab0 = browser.find_element(By.XPATH, '//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]')
    input_tab0.send_keys(Keys.ENTER)

    registration()


def registration():
    input_tab1 = browser.find_element(By.XPATH, '//*[@id="__next"]/header/div/div/div[3]/div/div[4]/button')
    input_tab1.send_keys(Keys.ENTER)

    sleep(2)
    input_tab2 = browser.find_element(By.XPATH, '//*[@id="username"]')
    input_tab2.send_keys('youremail@example.com')

    """Here you should enter email that you use on a website!"""

    input_tab3 = browser.find_element(By.XPATH, '//*[@id="password"]')
    input_tab3.send_keys('password')

    """Here you should enter password that you use on a website!"""

    input_tab3.send_keys(Keys.ENTER)

    search()


def search():
    sleep(3)
    input_tab4 = browser.find_element(By.XPATH, '//*[@id="__next"]/main/section[1]/div/div/div[2]/div[1]/div/div/div[1]/div/div[3]/div/div/label/input')
    input_tab4.send_keys('city')

    """Here you should enter city that you need!"""

    sleep(3)
    button = browser.find_element(By.XPATH, '//*[@id="react-autowhatever-1--item-1"]/button')
    button.click()

    sleep(3)
    browser.find_element(By.XPATH, '//*[@id="__next"]/main/section[1]/div/div/div[2]/div[1]/div/div/div[1]/div/div[4]/button').click()
    input_tab5 = browser.find_element(By.XPATH, '//*[@id="__next"]/main/section[1]/div/div/div[2]/div[1]/div/div/div[1]/div/div[4]/div/div/div[2]/input')
    input_tab5.send_keys('price')

    """Here you should enter price that you need!"""

    sleep(3)
    browser.find_element(By.XPATH, '//*[@id="__next"]/main/section[1]/div/div/div[2]/div[1]/div/div/div[2]/a').click()

    pages_parse()


def pages_parse():
    for page in range(1, 3):
        url = f'https://www.bezrealitky.cz/vyhledat?offerType=PRONAJEM&estateType=BYT&priceTo={10000}&page={page}&order=TIMEORDER_DESC&regionOsmIds=R435514&osm_value=Hlavn%C3%AD+m%C4%9Bsto+Praha%2C+Praha%2C+%C4%8Cesko'

        """Here you should enter price that you need!"""

        browser.get(url)
        sleep(5)

        soup = BeautifulSoup(browser.page_source, 'lxml')
        ads = soup.find_all('article', class_='PropertyCard_propertyCard__qPQRK')

        ads_parse(ads)


def ads_parse(ads):
    links = []
    for ad in ads:
        try:
            status = ad.find('span', class_='Tag_tag__Rns17')
            if status.text != 'Zobrazeno':
                link = ad.find('h2', class_='PropertyCard_propertyCardHeadline__y3bhA').find('a').get('href')
                links.append(link)
            else:
                print('Status was Zobrazeno!')
        except AttributeError:
            link = ad.find('h2', class_='PropertyCard_propertyCardHeadline__y3bhA').find('a').get('href')
            links.append(link)

    sending_message(links)


def sending_message(links):
    for url in links:
        browser.get(url)

        sleep(3)
        button = browser.find_element(By.XPATH, '//*[@id="__next"]/main/div[2]/section/div/div[2]/div/div/div[1]/p[2]/button')
        browser.execute_script("arguments[0].click();", button)

        sleep(3)
        form = browser.find_element(By.XPATH, '//*[@id="message"]')
        form.send_keys('''Your message''')

        """Here you should enter your message to the landlord!"""

        sleep(5)
        submit = browser.find_element(By.CSS_SELECTOR, 'body > div.fade.modal.show > div > div > div.modal-body > form > button')
        browser.execute_script("arguments[0].click();", submit)
    print('Messages have been sent!')