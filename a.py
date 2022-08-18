from selenium import webdriver
import unittest

class ATest(unittest.TestCase):

    baseURL = "https://amazon.com/"
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get(baseURL)
    print("Running tests on FF")
    driver.implicitly_wait(3)
    driver.quit()
