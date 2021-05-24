__author__ = "Christian Schramm & Leon Kasimir Koncebovski"
__version__ = "1.0.4"
__email__ = "schrammc@th-brandenburg.de"

import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep

import re

regex = re.compile('[^a-zA-Z]')  # nur alphabetische Nutzernamen


class Main:

    def __init__(self):
        self.browser = webdriver.Chrome('chromedriver.exe')
        self.browser.get("https://www.instagram.com/accounts/login/")

    def insta_login(self, username, password):
        username_web_element = self.browser.find_element_by_xpath("//input[@name=\"username\"]")
        username_web_element.send_keys(username)

        sleep(3)

        password_web_element = self.browser.find_element_by_xpath("//input[@name=\"password\"]")
        password_web_element.send_keys(password)

        login = self.browser.find_element_by_xpath("//button[@class=\"sqdOP  L3NKy   y3zKF     \"]")
        login.click()

        sleep(3)

    def facebook_login(self):
        savelogindata = self.browser.find_element_by_xpath("//button[@class=\"sqdOP yWX7d    y3zKF     \"]")
        savelogindata.click()

        sleep(2)

        acceptfacebook = self.browser.find_element_by_xpath(
            "//button[@class=\"_42ft _4jy0 _9o-t _4jy3 _4jy1 selected _51sy\"]")
        acceptfacebook.click()

        sleep(3)

        facebookskip = self.browser.find_element_by_class_name("_2iem")
        facebookskip.click()

        sleep(3)

    def save_insta_creds(self):
        saveinstacreds = self.browser.find_element_by_xpath("//button[@class=\"sqdOP yWX7d    y3zKF     \"]")
        saveinstacreds.click()

        sleep(2)

    def skip_notifications(self):
        skipNots = self.browser.find_element_by_xpath("//button[@class=\"aOOlW   HoLwm \"]")
        skipNots.click()

        sleep(2)

    def wait_for_object(self, type, string):
        return WebDriverWait(self.browser, 3).until(ec.presence_of_element_located((type, string)))

    def wait_for_objects(self, type, string):
        return WebDriverWait(self.browser, 3).until(ec.presence_of_all_elements_located((type, string)))

    def post_comments(self, hashtag, comment):
        sleep(2)

        random_comments = [comment]
        self.browser.get(f"https://www.instagram.com/explore/tags/{hashtag}/")

        pictures = self.wait_for_objects(By.CSS_SELECTOR, '._9AhH0')
        pictures[0].click()
        sleep(3)

        sleep(random.randint(2, 10))

        self.browser.get(f"https://www.instagram.com/explore/tags/{hashtag}/")

        pictures = self.wait_for_objects(By.CSS_SELECTOR, '._9AhH0')
        pictures[0].click()

        sleep(2)

        for i in range(0, 1):
            comments_box = self.wait_for_object(By.CSS_SELECTOR, '.Ypffh')
            comments_box.click()
            comments_box = self.wait_for_object(By.CSS_SELECTOR, '.Ypffh')
            comments_box.send_keys(random_comments[i])

            sleep(2)

            post_button = self.wait_for_object(By.XPATH, '//button[text()="Posten"]')
            post_button.click()

            sleep(random.randint(2, 10))


instance = Main()

cookies = instance.browser.find_element_by_xpath("//button[@class=\"aOOlW  bIiDR  \"]")
cookies.click()

sleep(5)

instance.insta_login("robbylindi123", "RobbyLindi1234")

instance.save_insta_creds()

instance.skip_notifications()
