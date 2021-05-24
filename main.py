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
        username = self.browser.find_element_by_xpath("//input[@name=\"username\"]")
        username.send_keys("robbylindi123")

        sleep(3)

        password = self.browser.find_element_by_xpath("//input[@name=\"password\"]")
        password.send_keys("RobbyLindi1234")

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
        skipnots = self.browser.find_element_by_xpath("//button[@class=\"aOOlW   HoLwm \"]")
        skipnots.click()

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

        self.browser.get(f"https://www.instagram.com/explore/tags/{hashtag}/")

        pictures = self.wait_for_objects(By.CSS_SELECTOR, '._9AhH0')
        pictures[0].click()
        sleep(3)

        for i in range(0, number_of_likes):
            sleep(2)
            likes = self.wait_for_objects(By.CSS_SELECTOR, 'svg[aria-label="Gefällt mir"]')
            likes[0].click()

            sleep(2)

            next_window = self.wait_for_object(By.CSS_SELECTOR, ' _65Bje.coreSpriteRightPaginationArrow')
            next_window.click()

            sleep(random.randint(2, 10))

    def post_comments(self, number_of_comments, hashtag_origin, hashtag_post):
        sleep(2)

        random_comments = [input("Bitte Kommentar eingeben: ")]
        self.browser.get(f"https://www.instagram.com/explore/tags/{hashtag_origin}/")

        pictures = self.wait_for_objects(By.CSS_SELECTOR, '._9AhH0')
        pictures[0].click()
        sleep(3)

        for i in range(0, number_of_comments):
            sleep(2)
            comments = self.wait_for_objects(By.XPATH, '//div[contains(@class, "C4VMK")]/span')
            sleep(2)
            comment = regex.sub(' ', comments[1].text)
            random_comments.append(comment)

            sleep(2)

            if i != number_of_comments - 1:
                next_window = self.wait_for_object(By.CSS_SELECTOR, ' _65Bje.coreSpriteRightPaginationArrow')
                next_window.click()

            sleep(random.randint(2, 10))

        self.browser.get(f"https://www.instagram.com/explore/tags/{hashtag_post}/")

        pictures = self.wait_for_objects(By.CSS_SELECTOR, '._9AhH0')
        pictures[0].click()

        sleep(2)

        for i in range(0, number_of_comments):
            comments_box = self.wait_for_object(By.CSS_SELECTOR, '.Ypffh')
            comments_box.click()
            comments_box = self.wait_for_object(By.CSS_SELECTOR, '.Ypffh')
            comments_box.send_keys(random_comments[i])

            sleep(2)

            post_button = self.wait_for_object(By.XPATH, '//button[text()="Posten"]')
            post_button.click()

            sleep(random.randint(2, 10))

            if i != number_of_comments - 1:
                next_window = self.wait_for_object(By.CSS_SELECTOR, ' _65Bje.coreSpriteRightPaginationArrow')
                next_window.click()

                sleep(random.randint(2, 10))


instance = Main()

cookies = instance.browser.find_element_by_xpath("//button[@class=\"aOOlW  bIiDR  \"]")
cookies.click()

sleep(5)

instance.insta_login("robbylindi123", "RobbyLindi1234")

instance.save_insta_creds()

instance.skip_notifications()

# instance.like_posts("Football", 3)

instance.post_comments(1, "Programminghumor", "Funny")
