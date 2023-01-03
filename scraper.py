import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (NoSuchElementException)
import re
import sys


def scrape_casa_it(driver):
    # Wait for the page to load the captcha
    driver.implicitly_wait(7)

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

    print('TITLE: ', title, end='\n\n')
    print('PRICE: ', price, end='\n\n')
    print('AREA: ', area, end='\n\n')
    print('ROOM COUNT: ', room_count, end='\n\n')
    print('ADDRESS: ', address, end='\n\n')
    print('COORDINATES: ', coordinates, end='\n\n')
    print('FEATURES: ', features, end='\n\n')
    print('DESCRIPTION: ', description, end='\n\n')


def scrape_urls(urls, website):
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    driver = uc.Chrome(options=options)

    with open('houses.txt', 'a') as output:
        original_stdout = sys.stdout
        sys.stdout = output
        for url in urls:
            # Navigate to webpage
            driver.get(url)
            print('\n================================================================================')
            print(url)
            print('================================================================================')
            if website['mailbox'] == 'CasaIT':
                try:
                    scrape_casa_it(driver)
                except NoSuchElementException as err:
                    print(err)
                    print('Probably got blocked by a captcha')
                    break
        sys.stdout = original_stdout
    driver.quit()
