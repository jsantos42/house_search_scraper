import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (NoSuchElementException)
import re
import csv


def scrape_casa_it(driver, url):
    # Wait for the page to load the captcha
    driver.implicitly_wait(5)

    # Title
    try:
        title = driver.find_element(By.XPATH, '//h1[@class="infos__H1"]').text
    except NoSuchElementException as err:
        if driver.find_element(By.XPATH, '//h1[@class="casa404--t tp-w--l c-txt--secondary"]').text == 'Pagina non trovata':
            print('No longer available')
            return
        else:
            print(err)
            title = ''

    # Price
    try:
        price = driver.find_element(By.XPATH, '//li[@class="infos__list__price"]').text
    except NoSuchElementException as err:
        print(err)
        price = ''

    # Area
    try:
        area = driver.find_element(By.XPATH, '//li[@class="infos__list__item is-rel"]').text
    except NoSuchElementException as err:
        print(err)
        area = ''

    # Room Count
    try:
        room_count = driver.find_element(By.XPATH, '//li[@class="infos__list__item is-rel infos__list__item--mlast"]').text
    except NoSuchElementException as err:
        print(err)
        room_count = ''

    # Address
    try:
        address = driver.find_element(By.XPATH, '//div[@class="grid boxed map grid grid--direction-column"]/div/p').text
        address += '\n' + driver.find_element(By.XPATH, '//div[@class="grid boxed map grid grid--direction-column"]/div/p[2]').text
    except NoSuchElementException as err:
        print(err)
        address = ''

    # Coordinates
    try:
        map_frame = driver.find_element(By.XPATH, '//div[@class="map__map is-rel"]')
        ActionChains(driver).scroll_to_element(map_frame).perform()
        img_src = driver.find_element(By.XPATH, '//div[@class="map__map is-rel"]/img').get_attribute('src')
        coord_pattern = re.compile(r'https://maps.googleapis.com/maps/api/staticmap\?center=(\d*\.\d*,\d*\.\d*)')
        coordinates = re.findall(coord_pattern, img_src)[0]
    except NoSuchElementException as err:
        print(err)
        coordinates = ''

    # Features
    features = driver.find_element(By.XPATH, '//ul[@class="chars__feats__list"]').text

    # Description
    try:
        description = driver.find_element(By.XPATH, '//div[@class="descr__desc"]').text
    except NoSuchElementException:
        try:
            description = driver.find_element(By.XPATH, '//div[@class="descr__desc descr__desc--closed"]').text
        except NoSuchElementException:
            try:
                description = driver.find_element(By.XPATH, '//div[@class="descr__desc descr__desc--open"]').text
            except NoSuchElementException as err:
                print(err)
                description = "Could not get description"
    return [url, title, area, room_count, address, coordinates, features, description]


def scrape_urls(urls, website):
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    driver = uc.Chrome(options=options)
    with open('houses.csv', 'a', newline='') as output:
        writer = csv.writer(output, delimiter=',', quoting=csv.QUOTE_ALL, doublequote=True)
        writer.writerow(['URL', 'Title', 'Price', 'Area', 'Room Count', 'Address', 'Coordinates', 'Features', 'Description'])
        for url in urls:
            # Navigate to webpage
            driver.get(url)
            if website['mailbox'] == 'CasaIT':
                try:
                    info = scrape_casa_it(driver, url)
                    writer.writerow(info)
                except NoSuchElementException as err:
                    print(err)
                    print('Probably got blocked by a captcha')
                    break
    driver.quit()
