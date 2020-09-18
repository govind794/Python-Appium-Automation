__author__ = 'Govind Patidar'

import unittest
import datetime
from selenium import webdriver


class EnvironmentSetup(unittest.TestCase):

    # setUP contains the app setup attributes
    def setUp(self):
        desired_cap = {
            "deviceName": "emulator-5554",
            "platformName": "Android",
            "app": "/Users/govind794/PycharmProjects/AppiumSandbox/app/com.flipkart.android.apk",
            "appPackage": "com.flipkart.android",
            "appWaitActivity": "com.flipkart.android.activity.MSignupActivity"
        }

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
        print("Run Started at :" + str(datetime.datetime.now()))
        print("App Environment Set Up")
        print("------------------------------------------------------------------")
        self.driver.implicitly_wait(20)

    # tearDown method just to close all the browser instances and then quit
    def tearDown(self):
        if (self.driver != None):
            print("------------------------------------------------------------------")
            print("Test Environment Destroyed")
            print("Run Completed at :" + str(datetime.datetime.now()))
            self.driver.close()
            self.driver.quit()
