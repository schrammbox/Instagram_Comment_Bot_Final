from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep


class Main:

    def __init__(self):
        self.browser = webdriver.Chrome('chromedriver.exe')
        self.browser.get("https://www.instagram.com/accounts/login/")

    def insta_login(self, username, password):
        username = self.browser.find_element_by_xpath("//input[@name=\"username\"]")
        username.send_keys("petermuenchi123")

        sleep(3)

        password = self.browser.find_element_by_xpath("//input[@name=\"password\"]")
        password.send_keys("PeterMünchi1234")

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

    '''def search_hashtag(self):
        searchvar = input("Bitte Hashtag eingeben: ")
        hashtag = self.browser.find_element_by_xpath("//input[@class=\"XTCLo  x3qfX \"]")
        hashtag.send_keys("#" + searchvar)
        hashtag.click()
        hashtag.click()
        '''

    def wait_for_object(self, type, string):
        return WebDriverWait(self.browser, 3).until(ec.presence_of_element_located((type, string)))

    def wait_for_objects(self, type, string):
        return WebDriverWait(self.browser, 3).until(ec.presence_of_all_elements_located((type, string)))

    def like_posts(self, hashtag, number_of_likes):

        self.browser.get(f"https://www.instagram.com/explore/tags/{hashtag}")

        pictures = self.wait_for_objects(By.CSS_SELECTOR, '._9AhH0')
        pictures[0].click()
        sleep(3)

        likes = self.wait_for_objects(By.CSS_SELECTOR, 'svg[aria-label="Gefällt mir"]')
        likes[0].click()

    def post_comments(self, number_of_comments, hashtag_origin, hashtag_post):
        comments_array = []
        # self.browser.get(f"https://www.instagram.com/explore/tags/{hashtag}")


instance = Main()

cookies = instance.browser.find_element_by_xpath("//button[@class=\"aOOlW  bIiDR  \"]")
cookies.click()

sleep(5)

instance.insta_login("petermuenchi123", "PeterMünchi1234")

instance.save_insta_creds()

instance.skip_notifications()

instance.like_posts(input("Bitte Hashtag eingeben: "), 3)
