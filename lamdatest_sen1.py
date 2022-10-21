


import time
import unittest
import sys
from selenium import webdriver
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
		        "build": "Test",
		        "project": "Untitled",
		        "name": "Testing",
		        "console": "true",
		        "selenium_version": "4.0.0",
		        "driver_version": "106.0",
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

                # """ You can write the test cases here """

    def test_demo_site(self):
        driver = self.driver
        driver.implicitly_wait(10)
        driver.set_page_load_timeout(30)
        driver.set_window_size(1920, 1080)

                # Url
        print('Loading URL')
        driver.get("https://www.lambdatest.com/selenium-playground")
        driver.find_element(By.PARTIAL_LINK_TEXT, "Simple Form Demo").click()
        driver.find_element(By.ID, "user-message").send_keys("Welcome to Lambdatest")
        driver.find_element(By.ID, "showInput").click()
        lamp = driver.find_element(By.ID, "message").text
        if lamp == 'Welcome to Lambdatest':
            print("True")

        else:
            print("False")
    time.sleep(10)

if __name__ == "__main__":
     unittest.main()

