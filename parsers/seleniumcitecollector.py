import re

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SeleniumCiteCollector():
    def __init__(self):
        self.driver = webdriver.Firefox()

    def get(self, url):
        self.driver.get(url)

    def findCites(self):
        try:
            element = WebDriverWait(self.driver, 60).until(
                EC.presence_of_element_located((By.PARTIAL_LINK_TEXT,  'Cited by'))
                )
            match = re.match('Cited by (\d+)', element.text)
            if match:
                return match.group(1)
        except TimeoutException as e:
            print (e)
        return None