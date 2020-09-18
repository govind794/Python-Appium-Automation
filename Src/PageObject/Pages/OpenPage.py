__author__ = 'Govind Patidar'

from appium.webdriver.common.mobileby import MobileBy

from Src.PageObject.Locators import Locator


class OpenPage(object):

    def __init__(self, driver):
        self.driver = driver

        # home page locators defining
        self.logo = driver.find_element(MobileBy.ID, Locator.logo)
        self.btn_skip = driver.find_element(MobileBy.ID, Locator.btn_skip)
        self.banner_text = driver.find_element(MobileBy.ID, Locator.banner_text)
        self.mobile_no = driver.find_element(MobileBy.ID, Locator.mobile_no)
        self.btn_msignup = driver.find_element(MobileBy.ID, Locator.btn_msignup)
        self.btn_mlogin = driver.find_element(MobileBy.ID, Locator.btn_mlogin)

    def getLogo(self):
        return self.logo

    def getBtnSkip(self):
        return self.btn_skip

    def getBannerText(self):
        return self.banner_text

    def getMobileNo(self):
        return self.mobile_no

    def getBtnMsignup(self):
        return self.btn_msignup

    def getBtnMlogin(self):
        return self.btn_mlogin
