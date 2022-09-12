import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

MY_GOOGLE_URL = os.environ.get('owm_form_url')
booking = 'https://www.booking.com/'
MY_BOOKING_URL = os.environ.get('owm_booking_url')
USER_AGENT = os.environ.get('owm_user_agent')


class BotBrain():
    """This class is responsible for bot behavior ."""
    def __init__(self):
        self.city = input("Your City:")
        self.date_from = input("Chek-in date (this month):")
        self.date_to = input("Departure date  (this month):")
        self.stars = int(input("Hotel class * - 2/3/4/5:"))
        self.s = Service('C:\Web development\chromedriver_win32\chromedriver.exe')

    def enter_data(self):
        """This function enters data on the booking page"""
        driver = webdriver.Chrome(service=self.s)
        driver.get(booking)
        time.sleep(1)
        enter_city = driver.find_element(By.XPATH, '//*[@id="ss"]')
        enter_city.send_keys(self.city)
        time.sleep(2)
        enter_date = driver.find_element(By.XPATH, '//*[@id="frm"]/div[1]/div[2]/div[1]/div[2]/div/div/div/div/span')
        enter_date.click()
        time.sleep(2)
        enter_push_date_from = driver.find_element(By.XPATH, f'//span[contains(text(), "{self.date_from}")]')
        enter_push_date_from.click()
        time.sleep(2)
        enter_push_date_to = driver.find_element(By.XPATH, f'//span[contains(text(), "{self.date_to}")]')
        enter_push_date_to.click()
        time.sleep(2)
        enter_push_enter = driver.find_element(By.XPATH, '//*[@id="frm"]/div[1]/div[4]/div[2]/button/span[1]')
        enter_push_enter.click()
        time.sleep(2)

        enter_push = driver.find_element(By.XPATH,
                                         f'//div[contains(text(), "{self.stars} {"звезды" if self.stars < 5 else "звезд"}")]')
        enter_push.click()

        return driver.current_url


    def fill_form(self, link_list, addres_list, price_list):
        """This function fills in the Google form data"""
        driver = webdriver.Chrome(service=self.s)

        for n in range(0, len(link_list)):
            driver.get(MY_GOOGLE_URL)
            time.sleep(2)

            enter_address = driver.find_element(By.XPATH,
                                                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            enter_address.send_keys(addres_list[n])

            enter_price = driver.find_element(By.XPATH,
                                              '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            enter_price.send_keys(price_list[n])

            enter_link = driver.find_element(By.XPATH,
                                             '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            enter_link.send_keys(link_list[n])

            enter_push = driver.find_element(By.XPATH,
                                             '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
            enter_push.click()
