
#************SCENARIO 3 ************

from selenium import webdriver
from selenium. webdriver. common. keys import Keys
from selenium.webdriver.common.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import unittest


username = "parnapalliharitha0"  # Replace the username
access_key = "VFHfq9pRwE0fBS0mXBnFpCwGkoJV4lbsgVeaLtP9cuJg141ePT"  # Replace the access key


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
                "build": "Testing3",
                "project": "Untitled",
                "name": "senario3",
                "console": "true",
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

    def tearDown(self):
         self.driver.quit()

                # """ You can write the test cases here """

    def test_demo_site(self):
        driver = self.driver
        driver.implicitly_wait(10)
        driver.set_page_load_timeout(30)
        driver.set_window_size(1920, 1080)

        print('Loading URL')



        driver.get("https://www.lambdatest.com/selenium-playground")
        driver.maximize_window()
        print("website opened correctly")
        time.sleep(2)
        # driver.find_element(By.CLASS_NAME,"inline-block").click()
        driver.find_element(By.LINK_TEXT, "Input Form Submit").click()
        driver.find_element(By.LINK_TEXT, "Input Form Submit").click()
        # driver.find_element(By.XPATH,"//*[@id="seleniumform"]/div[6]/button").perform()
        alt = driver.find_element(By.CSS_SELECTOR, "#seleniumform > div.text-right.mt-20 > button").click()
        assert "Please fill out this field" in "Please fill out this field"
        print("Please fill out this field")

        driver.find_element(By.ID, "name").send_keys("haritha")
       # time.sleep(2)
        driver.find_element(By.ID, "inputEmail4").send_keys("parnaplliharitha0@gmail.com")
        driver.find_element(By.ID, "inputPassword4").send_keys("123456")
        driver.find_element(By.NAME, "company").send_keys("xyzabc")
        driver.find_element(By.NAME, "website").send_keys("Lambdatest.com")
        # driver.find_element(By.NAME,"country").send_keys("#seleniumform > div:nth-child(3) > div.form-group.w-6\/12.smtablet\:w-full.pr-20.smtablet\:pr-0 > select > option:nth-child(104)").perform()
        driver.find_element(By.NAME, "country").send_keys("IN")
        driver.find_element(By.ID, "inputCity").send_keys("Atp")
        driver.find_element(By.NAME, "address_line1").send_keys("Ananthapur")
        driver.find_element(By.ID, "inputAddress2").send_keys("Singanamala")
        driver.find_element(By.ID, "inputState").send_keys("AP")
        driver.find_element(By.ID, "inputZip").send_keys("515435")
        time.sleep(5)
        # driver.find_element(By.XPATH,"//*[@id="inputZip"]").send_keys("515435")
        # driver.find_element(By.XPATH,"//*[@id="seleniumform"]/div[6]/button").click()
        # driver.find_element(By.CLASS_NAME,"btn btn-dark selenium_btn bg-black text-white hover:bg-lambda-900 py-5 px-10 rounded").click()
        driver.find_element(By.CSS_SELECTOR, "#seleniumform > div.text-right.mt-20 > button").click()

        # sub_text=sub.text
        assert "Thanks for contacting us, we will get back to you shortly" in "Thanks for contacting us, we will get back to you shortly"
        time.sleep(5)
        print("Successfully submitted")

if __name__ == "__main__":
     unittest.main()


