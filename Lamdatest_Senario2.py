import time
import unittest
import sys
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

username = "parnapalliharitha0"
access_key = "VFHfq9pRwE0fBS0mXBnFpCwGkoJV4lbsgVeaLtP9cuJg141ePT"


class FirstSampleTest(unittest.TestCase):
    # Generate capabilities from here: https://www.lambdatest.com/capabilities-generator/
    # setUp runs before each test case and
    def setUp(self):
        desired_caps = {
             "LT:Options": {
                 "username": "parnapalliharitha0",
                 "accessKey": "VFHfq9pRwE0fBS0mXBnFpCwGkoJV4lbsgVeaLtP9cuJg141ePT",
                 "video": True,
                 "platformName": "Windows 10",
                 "resolution": "1920x1080",
                 "network": True,
                 "build": "Scenario2",
                 "name": "drag&drop",
                 "selenium_version": "4.0.0",
                 "w3c": True,
                 "plugin": "python-pytest"

             },
             "browserName": "Chrome",
             "browserVersion": "106.0",

        }

        self.driver = webdriver.Remote(
            command_executor="https://parnapalliharitha0:VFHfq9pRwE0fBS0mXBnFpCwGkoJV4lbsgVeaLtP9cuJg141ePT@hub.lambdatest.com/wd/hub".format(username, access_key),
            desired_capabilities=desired_caps)

    # tearDown runs after each test case
    def tearDown(self):
        self.driver.quit()

    def test_unit_user_should_able_to_add_item(self):
        # try:
        driver = self.driver
        # Url
        driver.get('https://www.lambdatest.com/selenium-playground')
        driver.find_element(By.PARTIAL_LINK_TEXT, "Drag & Drop Sliders").click()
        drag = driver.find_element(By.XPATH, '//*[@id="slider3"]/div')
        ActionChains(driver).drag_and_drop_by_offset(drag, 99, 0).perform()

        drag1= driver.find_element(By.ID, "rangeSuccess").text
        time.sleep(5)

        print(drag1)


if __name__ == "__main__":
    unittest.main()